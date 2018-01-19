from requests import post
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
