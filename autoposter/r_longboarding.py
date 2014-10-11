import os
import praw


class RLongboarding(object):
    """An API for the /r/longboarding subreddit"""

    def __init__(self, reddit_api=praw.Reddit, subreddit='longboarding'):
        self.reddit = reddit_api(
            "/u/Widdershiny's Community Review Autoposter"
        )
        self.subreddit = subreddit

    def login(self):
        self.reddit.login(**self.credentials)

    def post_review(self, title, text):
        self.reddit.submit(
            self.subreddit,
            title,
            text=text)

    @property
    def credentials(self):
        return {
            "username": os.environ['REDDIT_USERNAME'],
            "password": os.environ['REDDIT_PASSWORD'],
        }
