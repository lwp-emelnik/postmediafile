import urllib
import requests


class BloggerPost:

    OAUTH2_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    OAUTH2_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'

    SCOPE_BLOGGER = 'https://www.googleapis.com/auth/blogger'
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    GRANT_AUTHORIZATION_CODE = 'authorization_code'

    def __init__(self, config):
        """
        Prepare an instance
        :param config: ConfigParser object
        """
        if not config['client_id'] or not config['client_secret']:
            raise Exception('Blogger post configuration is not fully filled')
        else:
            self.client_id = config['client_id']
            self.client_secret = config['client_secret']

        self.code = config['code'] if config['code'] else ''

    def get_auth_uri(self):
        """
        Prepare and return an url for authorization process
        :return:
        """
        params = {
            'client_id': self.client_id,
            'scope': self.SCOPE_BLOGGER,
            'redirect_uri': self.REDIRECT_URI,
            'response_type': 'code',
            'approval_prompt': 'force',
            'access_type': 'offline'
        }

        return self.OAUTH2_AUTH_URI + '?' + urllib.parse.urlencode(params)

    def create_post(self, data):
        if not self.code:
            raise Exception('Blogger post authorization code missing, please configure first')

        values = {
            'grant_type': self.GRANT_AUTHORIZATION_CODE,
            'code': self.code,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            #'scope': self.SCOPE_BLOGGER,
            'redirect_uri': self.REDIRECT_URI
        }

        print(values)

        response = requests.post(self.OAUTH2_TOKEN_URI, data=values)
        response_json = response.json()

        if response_json['error']:
            raise Exception('Failed to authorize: ' + response.text)

        access_token = response_json['access_token']
        token_type = response_json['token_type']

        # @todo Create post
