from calendar import timegm
from bento_map.settings import DATABASE_PROVIDER, DATABASE_COLLECTION, \
    DB_HOST_COLLECTION, HOST_COLLECTION, MAP_PROVIDER


class Model(object):

    def __init__(self, infra_name, name, created_at):
        self.infra_name = infra_name
        self.name = name
        self.created_at = created_at
        self.created_at_ts = timegm(self.created_at.timetuple())


class Database(Model):

    def __init__(
            self, infra_name, name, engine, env, project, team, offering,
            created_at
    ):
        super(Database, self).__init__(infra_name, name, created_at)
        self.engine = engine
        self.env = env
        self.project = project
        self.team = team
        self.offering = offering

    @property
    def collection(self):
        return DATABASE_COLLECTION

    @property
    def content(self):
        return {
            "action": "UPDATE",
            "collection": self.collection,
            "key": self.key,
            "element": {
                "id": self.infra_name,
                "name": self.name,
                "properties": {
                    "engine": self.engine,
                    "environment": self.env,
                    "project": self.project,
                    "team": self.team,
                    "offering": self.offering
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
                "timestamp": self.created_at_ts
            },
            "type": self.type
        }

    @property
    def key(self):
        return "{}/{}_{}".format(
            DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
        )

    @property
    def type(self):
        return "collections"


class Host(Model):

    def __init__(self, infra_name, name, identifier, created_at):
        super(Host, self).__init__(infra_name, name, created_at)
        self.identifier = identifier

    @property
    def collection(self):
        return DB_HOST_COLLECTION

    @property
    def type(self):
        return "edges"

    @property
    def content(self):
        return {
            "action": "UPDATE",
            "collection": self.collection,
            "key": self.key,
            "element": {
                "from": "{}/{}_{}".format(
                    DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
                ),
                "id": self.name,
                "name": self.name,
                "provider": DATABASE_PROVIDER,
                "timestamp": self.created_at_ts,
                "to": "{}/{}_{}".format(
                    HOST_COLLECTION, MAP_PROVIDER, self.identifier
                )
            },
            "type": self.type
        }

    @property
    def key(self):
        return "{}/{}_{}".format(
            DB_HOST_COLLECTION, DATABASE_PROVIDER, self.name
        )
