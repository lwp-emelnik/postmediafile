import urllib
import requests


class BloggerPost:

    OAUTH2_AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    OAUTH2_TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'

    SCOPE_BLOGGER = 'https://www.googleapis.com/auth/blogger'
    REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

    GRANT_AUTHORIZATION_CODE = 'authorization_code'
    GRANT_REFRESH_TOKEN = 'refresh_token'

    API_BLOGS = 'https://www.googleapis.com/blogger/v3/blogs/'

    def __init__(self, config):
        """
        Prepare an instance
        :param config: ConfigParser object
        """
        if 'client_id' not in config or 'client_secret' not in config or 'blog_id' not in config:
            raise Exception('Blogger post configuration is not fully filled, please see readme')

        self.client_id = config['client_id']
        self.client_secret = config['client_secret']
        self.blog_id = config['blog_id']
        self.code = config['code'] if 'code' in config else ''
        self.refresh_token = config['refresh_token'] if 'refresh_token' in config else ''

    def get_auth_uri(self):
        """
        Prepare and return an url for authorization process
        :return:
        """
        values = {
            'client_id': self.client_id,
            'scope': self.SCOPE_BLOGGER,
            'redirect_uri': self.REDIRECT_URI,
            'response_type': 'code',
            'approval_prompt': 'force',
            'access_type': 'offline'
        }

        return self.OAUTH2_AUTH_URI + '?' + urllib.parse.urlencode(values)

    def create_post(self, data):
        if not self.code:
            raise Exception('Blogger post authorization code missing, please configure first')

        # Work with access first
        headers = {'Content-Type': 'application/json'}

        values = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.REDIRECT_URI
        }

        if not self.refresh_token:
            # the first launch when the access/refresh token should be obtained
            values['grant_type'] = self.GRANT_AUTHORIZATION_CODE
            values['code'] = self.code
        else:
            # next launch when the access token should be get via refresh token
            values['grant_type'] = self.GRANT_REFRESH_TOKEN
            values['refresh_token'] = self.refresh_token

        response = requests.post(self.OAUTH2_TOKEN_URI, json=values, headers=headers)
        response_json = response.json()

        if 'access_token' not in response_json:
            raise Exception('Failed to authorize: ' + response.text)

        access_token = response_json['access_token']
        refresh_token = response_json['refresh_token'] if 'refresh_token' in response_json else self.refresh_token
        token_type = response_json['token_type']

        # Then add new post
        headers['Authorization'] = token_type + ' ' + access_token
        values = {
            'kind': 'blogger#post',
            'blog': {'id': self.blog_id},
            'title': data['title'],
            'content': data['text']
        }

        response = requests.post(self.API_BLOGS + self.blog_id + '/posts', json=values, headers=headers)
        response_json = response.json()

        if 'id' not in response_json:
            raise Exception('Failed to create post: ' + response.text)

        new_post_url = 'https://www.blogger.com/u/1/blog/post/edit/' + self.blog_id + '/' + response_json['id']

        return {
            'refresh_token': refresh_token,
            'new_post_url': new_post_url
        }
