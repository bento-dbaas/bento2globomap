import requests
from requests.auth import HTTPBasicAuth
from calendar import timegm
from datetime import datetime
from bento_map.settings import BENTO_ENDPOINT, HOST_PROVIDER_ENDPOINT, \
    HOST_PROVIDER_USER, HOST_PROVIDER_PASSWORD
from bento_map.models import Database, Host
from bento_map.loader import Loader


class Client(object):

    def __init__(self):
        self.databases = {}

    def _get(self, page=1):
        url = BENTO_ENDPOINT + '/api/host/'
        resp = requests.get(
            url, {'page': page, 'format': 'json'}, verify=False
        )
        if resp.ok:
            return resp.json()

    def get(self, base_date, only_page=None):
        page = 1
        if only_page:
            page = only_page

        has_more = True
        while has_more:
            resp = self._get(page)
            if resp is None:
                break

            for host in resp['host']:
                database = host.get('database', {})
                infra = database.get('infra', {})
                identifier = HostProvider.info(
                    "cloudstack", host.get('env_name'), host.get('identifier'),
                )["identifier"]
                yield Host(
                    infra.get('name'),
                    host.get('hostname'),
                    identifier,
                    base_date,
                )

                db_env = database['name'] + host.get('env_name')
                if db_env in self.databases:
                    continue

                self.databases[db_env] = True
                yield Database(
                    infra.get('name'),
                    database.get('name'),
                    database.get('engine'),
                    host.get('env_name'),
                    database.get('project_name'),
                    host.get('team_name'),
                    host.get('offering').get('type'),
                    base_date
                )

            if resp['_links']['next'] is None:
                has_more = False
            page += 1

    def send(self):
        timestamp = timegm(datetime.now().timetuple())
        loader = Loader()
        clear = {}
        for item in self.get(timestamp):
            print(loader.update(item))
            clear[item.collection] = item
        for collection in clear.values():
            print(loader.clear_old_data(collection, timestamp-1))


class HostProvider(object):

    @classmethod
    def info(cls, provider, environment, identifier):
        url = '{}/{}/{}/host/{}'.format(
            HOST_PROVIDER_ENDPOINT, provider, environment, identifier
        )
        auth = None
        if HOST_PROVIDER_USER:
            auth = HTTPBasicAuth(HOST_PROVIDER_USER, HOST_PROVIDER_PASSWORD)
        response = requests.get(url, auth=auth, verify=False)
        if response.ok:
            print(response.json())
            return response.json()
        raise EnvironmentError(
            "Could not load info about host: \n{}\n{}-{}".format(
                url, response.status_code, response.content
            )
        )
