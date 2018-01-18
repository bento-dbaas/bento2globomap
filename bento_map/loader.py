from requests import post
from bento_map.settings import MAP_ENDPOINT


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
    return post(url, json=content)
