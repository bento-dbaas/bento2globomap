from datetime import datetime, timedelta
from time import sleep
from requests import get, post
from bento_map.settings import MAP_ENDPOINT, BOT_ENDPOINT


def build_clear_to(collections, before):
    content = []
    for collection, map_type in collections.items():
        content.append({
            "action": "CLEAR",
            "collection": collection,
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": before - 1
            }]],
            "type": map_type
        })
    return content


def build_model_payload(models):
    content = []
    collections = {}
    for model in models:
        content.append(model.content)
        collections[model.collection] = model.type

    return content, collections


def build_full_payload(models, before):
    content, collections = build_model_payload(models)
    content += build_clear_to(collections, before)
    return content


def update(models, before):
    content = build_full_payload(models, before)
    url = MAP_ENDPOINT + "/v1/updates"
    response = post(url, json=content)
    response_json = response.json()

    if response.ok:
        return True, response_json["jobid"]

    error = response_json["errors"]
    notify_bot(error)
    return False, error


def notify_bot(error):
    json = {"message": "Error sending content to Map: {}".format(error)}
    return post(BOT_ENDPOINT + "/notify", json=json)


def get_job_status(job_id):
    url = MAP_ENDPOINT + "/v1/updates/job/{}".format(job_id)
    response = get(url)

    if not response.ok:
        notify_bot("{} - {}".format(response.status_code, response.content))
        return True

    json = response.json()
    errors = json["errors"]
    if json["completed"] and errors:
        notify_bot(errors)

    return json["completed"]


def wait_job_be_done(job_id, timeout_second=1800, wait=15):
    end_at = datetime.now() + timedelta(seconds=timeout_second)
    while end_at > datetime.now():
        done = get_job_status(job_id)
        if done:
            break

        sleep(wait)
