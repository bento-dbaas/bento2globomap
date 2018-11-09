from logging import info
from requests import post
from globomap_loader_api_client.auth import Auth
from globomap_loader_api_client.update import Update
from bento_map.settings import MAP_ENDPOINT, MAP_USERNAME, MAP_PASSWORD, \
    BOT_ENDPOINT, DATABASE_PROVIDER


class Loader(object):
    def __init__(self):
        self.auth = Auth(
            api_url=MAP_ENDPOINT,
            username=MAP_USERNAME,
            password=MAP_PASSWORD
        )
        self.provider = DATABASE_PROVIDER

    def clear_old_data(self, model, before):
        content = {
            "action": "CLEAR",
            "collection": model.collection,
            "element": [[{
                "field": "timestamp",
                "operator": "<",
                "value": before
            }]],
            "type": model.type
        }
        return self.__execute(content)

    def update(self, model):
        return self.__execute(model.content)

    def __execute(self, content):
        try:
            info(content)
            update = Update(auth=self.auth, driver_name=self.provider)
            response = update.post(content)
            info(response)
            return response
        except Exception as e:
            self.notify_bot(str(e))
            raise e

    @staticmethod
    def notify_bot(error):
        json = {"message": "Error sending content to Map: {}".format(error)}
        return post(BOT_ENDPOINT + "/notify", json=json)
