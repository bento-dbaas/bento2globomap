from unittest import TestCase
from calendar import timegm
from datetime import datetime
from bento_map.models import Database, Host
from bento_map.settings import DATABASE_PROVIDER, DATABASE_COLLECTION, \
    DB_HOST_COLLECTION, HOST_COLLECTION, MAP_PROVIDER


class TestCreateDatabase(TestCase):

    def _test_content(
            self, identifier, name, engine, env, project, team, offering,
            created_at
    ):
        database = Database(
            identifier, name, engine, env, project, team, offering, created_at
        )
        base = {
            "action": "CREATE",
            "collection": DATABASE_COLLECTION,
            "element": {
                "id": identifier,
                "name": name,
                "properties": {
                    "engine": engine,
                    "environment": env,
                    "project": project,
                    "team": team,
                    "offering": offering,
                },
                "properties_metadata": {
                    "engine": {
                        "description": "Database engine"
                    },
                    "offering": {
                        "description": "Offering of cluster machines"
                    },
                    "environment": {
                        "description": "Environment where is database"
                    },
                    "project": {
                        "description": "Database owner project"
                    },
                    "team": {
                        "description": "Database owner team"
                    }
                },
                "provider": DATABASE_PROVIDER,
                "timestamp": timegm(created_at.timetuple()),
            },
            "type": "collections"
        }
        self.assertDictEqual(database.content, base)

    def test_basic_redis(self):
        self._test_content(
            "fakeredis123456", "fake_redis", "redis-4.0.2", "dev", "bento-map",
            "bento-db", "1*2cpu4096mb", datetime.now()
        )

    def test_basic_mysql(self):
        self._test_content(
            "fakemysql889977", "fake_mysql", "mysql-5.6.24", "prod",
            "batman-api", "justice-league", "2*1cpu2048mb",
            datetime(2018, 2, 15, 17, 35, 1)
        )


class TestCreateDatabaseCompUnit(TestCase):

    def _test_content(
            self, infra_name, name, identifier, created_at
    ):
        host = Host(infra_name, name, identifier, created_at)
        base = {
            "action": "CREATE",
            "collection": DB_HOST_COLLECTION,
            "element": {
                "from": "{}/{}_{}".format(
                    DATABASE_COLLECTION, DATABASE_PROVIDER, infra_name
                ),
                "id": name,
                "name": name,
                "provider": DATABASE_PROVIDER,
                "timestamp": timegm(created_at.timetuple()),
                "to": "{}/{}_{}".format(
                    HOST_COLLECTION, MAP_PROVIDER, identifier
                )
            },
            "type": "edges"
        }
        self.assertDictEqual(host.content, base)

    def test_host_redis(self):
        self._test_content(
            "fakeredis123456", "fakeredis-01-123456", "a76ax-b3bu-2cd4-cjjc",
            datetime.now()
        )

    def test_host_mysql(self):
        self._test_content(
            "fakemysql889977", "fakemysql-01-889977", "a76ax-b3bb-2cd4-cd3c",
            datetime(2018, 2, 15, 17, 30, 15)
        )
        self._test_content(
            "fakemysql889977", "fakemysql-02-889977", "a76aa-b3bb-2cc4-cd2c",
            datetime(2018, 2, 15, 17, 33, 13)
        )
