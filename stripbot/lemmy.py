import os
import time

import requests
from decouple import config


class Lemmy:
    def __init__(self) -> None:
        self.jwt = None

    @staticmethod
    def build_url(endpoint):
        return config('LEMMY_BASEURL')+'/api/v3/'+endpoint

    def login(self):
        data = {
            'username_or_email': config('LEMMY_USERNAME'),
            'password': config('LEMMY_PASSWORD'),
        }
        
        login = requests.post(self.build_url('user/login'), json=data)
        result = login.json()
        self.jwt = result['jwt']


    def create_post(self, comic):
        if self.jwt is None:
            self.login()

        data = {
            'name': comic.post_title,
            'url': comic.post_url,
            'body': "",
            'nsfw': False,
            'community_id': config('LEMMY_COMMUNITY_ID', cast=int),
            'auth': self.jwt,
        }
        post = requests.post(self.build_url('post'), json=data).json()
        post_id = post['post_view']['post']['id']
        print(f"Post {post_id} posted successfully!")




# def post_comic(comic):
#     api = get_reddit()
#     time.sleep(2)

#     subreddit = os.environ.get('STRIPPOSTER_SUBREDDIT',
#                                '/r/testingground4bots')

#     if subreddit.startswith('/r/'):
#         subreddit = subreddit[3:]

#     subreddit = api.subreddit(subreddit)

#     # try:
#     #     reddit_post = subreddit.submit(comic.post_title,
#     #                                    url=comic.post_url,
#     #                                    resubmit=True,
#     #                                    send_replies=False)
#     #     comment = comic.post_comment
#     #     if comment:
#     #         comment = comment.rstrip() + "\n\n"

#     #     comment += (
#     #         "Ik ben een bot, _bliep_, _bloep_. Ik probeer strips te plaatsen "
#     #         "kort  nadat de auteur ze online zet. Vind je dat ik en strip mis,"
#     #         " of denk je dat er iets mis gaat? Maak dan een "
#     #         "[issue](https://github.com/ondergetekende/stripposter/issues) "
#     #         "aan. Ik word beheerd door /u/kvdveer")

#     #     reddit_post.reply(comment)
#     # except praw.errors.AlreadySubmitted:
#     #     pass
