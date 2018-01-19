from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from json import dumps
from requests import Response
from bento_map.loader import build_clear_to, build_model_payload, \
    build_full_payload, update, notify_bot, get_job_status
from bento_map.models import Host, Database
from bento_map.settings import MAP_ENDPOINT, BOT_ENDPOINT


class TestLoader(TestCase):

    def _dict_to_binary(self, dictionary):
        content = dumps(dictionary)
        return content.encode()

    def test_build_clear(self):
        build = build_clear_to({"fake": "edge", "bento": "collection"}, 1000)
        base = [{
            "action": "CLEAR",
            "collection": "fake",
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": 999
            }]],
            "type": "edge"
        }, {
            "action": "CLEAR",
            "collection": "bento",
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": 999
            }]],
            "type": "collection"
        }]
        self.assertEqual(build, base)

    def _build_models(self):
        date = datetime.now()
        database = Database(
            "fake12345", "fake", "cassandra", "qa", "heroes", "dc", "strong",
            date
        )
        host_1 = Host(
            "fake12345", "fake-01-12345", "1234-4321-1234-4321", date
        )
        host_2 = Host(
            "fake12345", "fake-02-12345", "5678-8765-5678-8765", date
        )
        return database, host_1, host_2

    def _validated_collections(self, collections, database, host_1, host_2):
        self.assertEqual(len(collections), 2)
        self.assertIn(database.collection, collections)

        self.assertEqual(collections[database.collection], database.type)
        self.assertIn(host_1.collection, collections)
        self.assertEqual(collections[host_1.collection], host_2.type)

    def test_build_model_payload(self):
        database, host_1, host_2 = self._build_models()
        content, collections = build_model_payload([database, host_1, host_2])
        self._validated_collections(collections, database, host_1, host_2)
        self.assertEqual(len(content), 3)
        self.assertDictEqual(content[0], database.content)
        self.assertDictEqual(content[1], host_1.content)
        self.assertDictEqual(content[2], host_2.content)

    def _validated_clear_content(self, content, before):
        base = {
            "action": "CLEAR",
            "collection": content["collection"],
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": before
            }]],
            "type": content["type"]
        }
        self.assertDictEqual(base, content)

    def test_build_full_payload(self):
        database, host_1, host_2 = self._build_models()
        content = build_full_payload([database, host_1, host_2], 5001)
        self.assertEqual(len(content), 5)
        self.assertDictEqual(content[0], database.content)
        self.assertDictEqual(content[1], host_1.content)
        self.assertDictEqual(content[2], host_2.content)
        self._validated_clear_content(content[3], 5000)
        self._validated_clear_content(content[4], 5000)

    @patch("bento_map.loader.post")
    def test_update_content(self, post):
        job_id = "123-456-789"
        expected = {
            "jobid": job_id, "message": "Updates published successfully"
        }
        response = Response()
        response.status_code = 202
        response._content = self._dict_to_binary(expected)
        post.return_value = response

        before = 88888
        models = self._build_models()
        content = build_full_payload(models, before)

        success, generated_job_id = update(models, before)

        self.assertTrue(success)
        self.assertEqual(job_id, generated_job_id)
        post.assert_called_once_with(
            MAP_ENDPOINT + "/v1/updates", json=content
        )

    @patch("bento_map.loader.post")
    def test_update_error(self, post):
        expected = {
            "errors": [{
                "error_pointer": "#/", "error_reasons": ["Wrong type"]
            }]
        }
        response = Response()
        response.status_code = 400
        response._content = self._dict_to_binary(expected)
        post.return_value = response

        models = self._build_models()
        success, error = update(models, 8888)

        self.assertFalse(success)
        self.assertEqual(expected["errors"], error)

    @patch("bento_map.loader.post")
    def test_bot_notify(self, post):
        error = "Fake test"
        expected = {
            "message": "Error sending content to Map: {}".format(error)
        }
        notify_bot(error)
        post.assert_called_once_with(
            BOT_ENDPOINT + "/notify", json=expected
        )

    def _validated_get_job_status(
            self, get, completed, errors, status_code
    ):
        job_id = "123456-9959-0050-7777123"
        expected = {
            "completed": completed,
            "errors": errors,
            "uuid": job_id
        }

        response = Response()
        response.status_code = status_code
        response._content = self._dict_to_binary(expected)
        get.return_value = response

        response = get_job_status(job_id)
        self.assertEqual(response, completed)

        get.assert_called_once_with(
            MAP_ENDPOINT + "/v1/updates/job/{}".format(job_id)
        )

    @patch("bento_map.loader.get")
    def test_get_job_status(self, get):
        self._validated_get_job_status(get, True, [], 200)

    @patch("bento_map.loader.get")
    @patch("bento_map.loader.notify_bot")
    def test_get_job_status_error_running(self, notify_bot, get):
        self._validated_get_job_status(get, False, ["Fake", "error"], 200)
        notify_bot.assert_not_called()

    @patch("bento_map.loader.get")
    @patch("bento_map.loader.notify_bot")
    def test_get_job_status_error_completed(self, notify_bot, get):
        errors = ["Fake", "error"]
        self._validated_get_job_status(get, True, errors, 200)
        notify_bot.assert_called_once_with(errors)

    @patch("bento_map.loader.get")
    @patch("bento_map.loader.notify_bot")
    def test_get_job_status_api_error(self, notify_bot, get):
        errors = ["Fake", "error"]
        self._validated_get_job_status(get, True, errors, 404)
        notify_bot.assert_called_once_with(
            "{} - {}".format(
                get.return_value.status_code, get.return_value.content
            )
        )
