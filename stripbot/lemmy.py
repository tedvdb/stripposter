import requests
from decouple import config


class Lemmy:
    def __init__(self) -> None:
        self.jwt = None

    @staticmethod
    def build_url(endpoint):
        return config('LEMMY_BASEURL')+'/api/v3/'+endpoint

    def login(self):
        username = config('LEMMY_USERNAME')
        data = {
            'username_or_email': username,
            'password': config('LEMMY_PASSWORD'),
        }
        
        login = requests.post(self.build_url('user/login'), json=data)
        result = login.json()
        self.jwt = result['jwt']
        print(f"Logged in as {username}.")


    def create_post(self, comic):
        if self.jwt is None:
            self.login()

        data = {
            'name': comic.post_title,
            'url': comic.post_url,
            'body': "",
            'nsfw': False,
            'community_id': config('LEMMY_COMMUNITY_ID', cast=int),
        }
        headers = {
            "accept": "application/json",
            "authorization": f"Bearer {self.jwt}"
        }
        post = requests.post(self.build_url('post'), json=data, headers=headers).json()
        print(post)
        post_id = post['post_view']['post']['id']
        print(f"Post {post_id} posted successfully!")
