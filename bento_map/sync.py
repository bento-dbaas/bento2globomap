from logging import info, basicConfig, getLogger, INFO
from time import sleep
from bento_map.client import Client


basicConfig()
getLogger().setLevel(INFO)


def sync():
    while True:
        info("Syncing data with Bento to Map")
        client = Client()
        client.send()
        info("Done")
        sleep(60*15)


if __name__ == '__main__':
    sync()
