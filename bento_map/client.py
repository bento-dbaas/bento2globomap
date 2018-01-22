import requests
from calendar import timegm
from datetime import datetime
from bento_map.settings import BENTO_ENDPOINT
from bento_map.models import Database, Host
from bento_map.loader import update, wait_job_be_done



class Client(object):

    def __init__(self):
        self.databases = {}

    def _get(self, page=1):
        url = BENTO_ENDPOINT + '/api/host/'
        resp = requests.get(url, {'page': page, 'format': 'json'})

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
                yield Host(
                    infra.get('name'),
                    host.get('hostname'),
                    host.get('identifier'),
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

            has_more = False
            if resp['_links']['next'] is None:
                has_more = False

            page += 1

    def sent(self):
        date = datetime.now()
        date_ts = timegm(date.timetuple())

        jobs = []
        errors = []
        for page in range(200):
            print('Loading page:', page)
            content = list(self.get(date, page))
            print('  Done')

            if not content:
                break

            success, job_id = update(content, date_ts)
            if success:
                jobs.append(job_id)
            else:
                errors.append(job_id)

        for job in jobs:
            print('Waiting: ;', job)
            wait_job_be_done(job)
            print('  Done')
