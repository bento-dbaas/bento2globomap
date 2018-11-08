from bento_map.settings import DATABASE_PROVIDER, DATABASE_COLLECTION, \
    DB_HOST_COLLECTION, HOST_COLLECTION, MAP_PROVIDER, DB_TSURU_COLLECTION


class BaseModel(object):

    def __init__(self, infra_name, name, timestamp):
        self.infra_name = infra_name
        self.name = name
        self.timestamp = timestamp

    @property
    def collection(self):
        raise NotImplementedError

    @property
    def key(self):
        raise NotImplementedError

    @property
    def element(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def content(self):
        return {
            "action": "UPDATE",
            "collection": self.collection,
            "key": self.key,
            "type": self.type,
            "element": self.element
        }


class Database(BaseModel):

    def __init__(
            self, infra_name, name, engine, env, project, team, offering,
            timestamp
    ):
        super(Database, self).__init__(infra_name, name, timestamp)
        self.engine = engine
        self.env = env
        self.project = project
        self.team = team
        self.offering = offering

    @property
    def collection(self):
        return DATABASE_COLLECTION

    @property
    def key(self):
        return "{}_{}".format(
            DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
        )

    @property
    def type(self):
        return "collections"

    @property
    def element(self):
        return {
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
            "timestamp": self.timestamp
        }


class Host(BaseModel):

    def __init__(self, infra_name, name, identifier, timestamp):
        super(Host, self).__init__(infra_name, name, timestamp)
        self.identifier = identifier
        self.full_name = self.name
        self.name = name.split(".", maxsplit=1)[0]

    @property
    def collection(self):
        return DB_HOST_COLLECTION

    @property
    def type(self):
        return "edges"

    @property
    def element(self):
        return {
            "from": "{}/{}_{}".format(
                DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
            ),
            "id": self.name,
            "name": self.name,
            "provider": DATABASE_PROVIDER,
            "timestamp": self.timestamp,
            "to": "{}/{}_{}".format(
                HOST_COLLECTION, MAP_PROVIDER, self.identifier
            )
        }

    @property
    def key(self):
        return "{}_{}".format(
            DB_HOST_COLLECTION, DATABASE_PROVIDER, self.name
        )

class Tsuru(BaseModel):

    def __init__(self, infra_name, name, identifier, timestamp):
        super(Tsuru, self).__init__(infra_name, name, timestamp)
        self.identifier = identifier
        self.full_name = self.name
        self.name = name.split(".", maxsplit=1)[0]

    @property
    def collection(self):
        return DB_TSURU_COLLECTION

    @property
    def type(self):
        return "edges"

    @property
    def element(self):
        return {
            "from": "{}/{}_{}".format(
                DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
            ),
            "id": self.name,
            "name": self.name,
            "provider": DATABASE_PROVIDER,
            "timestamp": self.timestamp,
            "to": "{}/{}_{}".format(
                HOST_COLLECTION, MAP_PROVIDER, self.identifier
            )
        }

    @property
    def key(self):
        return "{}_{}".format(
            DB_HOST_COLLECTION, DATABASE_PROVIDER, self.name
        )
