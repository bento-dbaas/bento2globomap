from requests import post
from bento_map.settings import MAP_ENDPOINT


def update(models):
    content = list()
    collections = {}
    lower_timestamp = None
    for model in models:
        content.append(model.content)
        collections[model.collection] = model.type

        if not lower_timestamp:
            lower_timestamp = model.created_at_ts
        if lower_timestamp > model.created_at_ts:
            lower_timestamp = model.created_at_ts

    for collection, type in collections.items():
        content.append({
            "action": "CLEAR",
            "collection": collection,
            "element": [
                [
                    {
                    "field": "timestamp",
                        "operator": "<",
                        "value": lower_timestamp
                    }
                ]
            ],
            "type": type
        })

    url = MAP_ENDPOINT + "/v1/updates"
    print(content)

    return post(url, json=content)
