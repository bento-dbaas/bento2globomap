from requests import post
from bento_map.settings import MAP_ENDPOINT


def update(models, remove_before_at):
    content = list()
    collections = {}
    for model in models:
        content.append(model.content)
        collections[model.collection] = model.type

    for collection, collection_type in collections.items():
        content.append({
            "action": "CLEAR",
            "collection": collection,
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": remove_before_at - 1
            }]],
            "type": collection_type
        })

    url = MAP_ENDPOINT + "/v1/updates"
    return post(url, json=content)
