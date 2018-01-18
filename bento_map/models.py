from bento_map.settings import DATABASE_PROVIDER, DATABASE_COLLECTION, \
    DB_HOST_COLLECTION, HOST_COLLECTION, MAP_PROVIDER


class Database(object):

    def __init__(
            self, infra_name, name, engine, env, project, team, offering,
            created_at
    ):
        self.infra_name = infra_name
        self.name = name
        self.engine = engine
        self.env = env
        self.project = project
        self.team = team
        self.offering = offering
        self.created_at = created_at

    @property
    def content(self):
        return {
            "action": "CREATE",
            "collection": DATABASE_COLLECTION,
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
                "timestamp": self.created_at
            },
            "type": "collections"
        }


class Host(object):

    def __init__(self, infra_name, name, identifier, created_at):
        self.infra_name = infra_name
        self.name = name
        self.identifier = identifier
        self.created_at = created_at


    @property
    def content(self):
        return {
            "action": "CREATE",
            "collection": DB_HOST_COLLECTION,
            "element": {
                "from": "{}/{}_{}".format(
                    DATABASE_COLLECTION, DATABASE_PROVIDER, self.infra_name
                ),
                "id": self.name,
                "name": self.name,
                "provider": DATABASE_PROVIDER,
                "timestamp": self.created_at,
                "to": "{}/{}_{}".format(
                    HOST_COLLECTION, MAP_PROVIDER, self.identifier
                )
            },
            "type": "edges"
        }
