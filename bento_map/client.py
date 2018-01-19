import requests
from datetime import datetime
from bento_map.models import Host


API = 'http://localhost:8000/api/host/'


class Client(object):

    def _get(self, page=1):
        resp = requests.get(API, params={'page': page, 'format': 'json'})

        if resp.ok:
            return resp.json()

    def get(self):
        page = 1
        has_more = True
        while has_more:
            resp = self._get(page)
            if resp is None:
                break
            for host in resp['host']:
                yield Host(
                    infra_name=host.get('database', {}).get('infra', {}).get('name'),
                    name=host.get('hostname'),
                    identifier=host.get('identifier'),
                    created_at=datetime.now(),
                )
            if resp['_links']['next'] is None:
                has_more = False
            page += 1
