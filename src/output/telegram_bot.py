import requests


class TelegramBot:

    API_ENDPOINT_URL = 'https://api.telegram.org/bot'
    GET_UPDATES_PATH = 'getUpdates'
    SEND_MESSAGE_PATH = 'sendMessage'
    SEND_VIDEO_PATH = 'sendVideo'

    def __init__(self, config):
        """
        Prepare an instance
        :param config: ConfigParser object
        """
        if 'token' not in config or 'chat_id' not in config:
            raise Exception('Telegram bot configuration is not fully filled')
        else:
            self.token = config['token']
            self.chat_id = config['chat_id']

    def get_url(self, path):
        """
        :param path: End part of the url
        :return: Full resulting url
        """
        return self.API_ENDPOINT_URL + self.token + '/' + path

    def get_updates(self):
        """
        Get list og updates
        :return:
        """
        response = requests.get(self.get_url(self.GET_UPDATES_PATH))
        response_json = response.json()

        if 'ok' not in response_json:
            raise Exception('Failed to get updates: ' + response.text)

        return response_json['result']

    def send_data(self, data):
        """
        Send a message with an attached videofile
        :param data:
        :return:
        """
        caption = data['title'] + '\n\n' + data['text']

        files = {
            'video': open(data['sidecar_file_name'], 'rb')
        }

        values = {
            'chat_id': self.chat_id,
            'caption': caption,
            # 'parse_mode': 'MarkdownV2'
        }

        response = requests.post(self.get_url(self.SEND_VIDEO_PATH), files=files, data=values)
        response_json = response.json()

        if 'ok' not in response_json:
            raise Exception('Failed to send data: ' + response.text)

        return response_json['result']
