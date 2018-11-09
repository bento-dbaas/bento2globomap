from time import sleep
from bento_map.client import Client


def sync():
    while True:
        print("Syncing data with Bento to Map")
        client = Client()
        client.send()
        print("Done")
        sleep(60*15)


if __name__ == '__main__':
    sync()
