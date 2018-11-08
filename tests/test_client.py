from copy import deepcopy
from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from bento_map.client import Client
from tests.fakes.host import HOST_API_PAGE_1, HOST_API_PAGE_2  #noqa


class FakeResponse(object):

    def __init__(self, resp):
        self.resp = resp

    @property
    def ok(self):
        return True

    def json(self):
        return self.resp


def fake_full_get(*args, **kw):
    page = args[1].get('page')
    return fake_get('full', page)


def fake_small_get(*args, **kw):
    page = args[1].get('page')
    return fake_get('small', page)


def fake_get(size, page):
    fake_resp = deepcopy(globals()['HOST_API_PAGE_{}'.format(page)])
    if size == 'small':
        fake_resp['host'] = fake_resp['host'][:1]
    return FakeResponse(fake_resp)


class ClientTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('bento_map.client.requests.get', side_effect=fake_full_get)
    def test_get_hosts(self, get_mock):
        hosts = self.client.get(datetime.now())

        host1 = next(hosts)
        next(hosts)
        host2 = next(hosts)

        self.assertEqual(host1.infra_name, 'fake_infra_name1')
        self.assertEqual(host1.name, 'fake_hostname1')
        self.assertEqual(host1.identifier, 'fake_identifier1')
        self.assertEqual(host2.infra_name, 'fake_infra_name2')
        self.assertEqual(host2.name, 'fake_hostname2')
        self.assertEqual(host2.identifier, 'fake_identifier2')

    @patch('bento_map.client.requests.get', side_effect=fake_small_get)
    def test_pagination(self, get_mock):
        hosts = self.client.get(datetime.now())
        host1 = next(hosts)
        next(hosts)
        host2 = next(hosts)

        self.assertEqual(host1.infra_name, 'fake_infra_name1')
        self.assertEqual(host1.name, 'fake_hostname1')
        self.assertEqual(host1.identifier, 'fake_identifier1')
        self.assertEqual(host2.infra_name, 'fake_infra_name1_page2')
        self.assertEqual(host2.name, 'fake_hostname1_page2')
        self.assertEqual(host2.identifier, 'fake_identifier1_page2')
