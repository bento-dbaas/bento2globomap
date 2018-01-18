from os import getenv


DATABASE_PROVIDER = getenv("DATABASE_PROVIDER", "bento")
MAP_PROVIDER = getenv("MAP_PROVIDER", "map")

DATABASE_COLLECTION = getenv("DATABASE_COLLECTION", "db")
DB_HOST_COLLECTION = getenv("DB_HOST_COLLECTION", "vm_db")
HOST_COLLECTION = getenv("HOST_COLLECTION", "vm")
