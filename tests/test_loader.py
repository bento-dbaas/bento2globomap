from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from bento_map.loader import build_clear_to, build_model_payload, \
    build_full_payload, update
from bento_map.models import Host, Database
from bento_map.settings import MAP_ENDPOINT


class TestLoader(TestCase):

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
            "fake12345", "fake", "cassandra", "qa", "heroes", "dc", "strong", date
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
    def test_update(self, post):
        post.return_value = 202

        before = 88888
        models = [self._build_models()[0]]
        result = update(models, before)

        content = build_full_payload(models, before)

        self.assertEqual(post.return_value, result)
        post.assert_called_once_with(
            MAP_ENDPOINT + "/v1/updates", json=content
        )