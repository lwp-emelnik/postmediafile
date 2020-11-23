import requests


class TelegramBot:

    url = 'https://api.telegram.org/bot'

    def __init__(self, config):
        """
        Prepare an instance
        :param config: ConfigParser object
        """
        if not config['token'] or not config['chat_id']:
            raise Exception('Telegram bot configuration is not fully filled')
        else:
            self.token = config['token']
            self.chat_id = config['chat_id']

    def get_url(self, path):
        """
        :param path: End part of the url
        :return: Full resulting url
        """
        return self.url + self.token + '/' + path

    def get_updates(self):
        """
        Get list og updates
        :return:
        """
        response = requests.get(self.get_url('getUpdates'))
        return response.json()['result']
