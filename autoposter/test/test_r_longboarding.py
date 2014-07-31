import autoposter

import pytest
import os
from unittest.mock import MagicMock

TEST_CREDENTIALS = {
    "username": 'test',
    "password": 'swordfish'
}


def set_test_credentials():
    os.environ['REDDIT_USERNAME'] = TEST_CREDENTIALS['username']
    os.environ['REDDIT_PASSWORD'] = TEST_CREDENTIALS['password']


@pytest.fixture
def r_longboarding():
    fake_reddit = MagicMock(autospec='praw.Reddit')
    api = autoposter.RLongboarding(reddit_api=lambda name: fake_reddit)
    return api


class TestRLongboarding(object):

    def test_login(self, r_longboarding):
        set_test_credentials()
        r_longboarding.login()

        r_longboarding.reddit.login.assert_called_with(
            **r_longboarding.credentials
        )

    def test_posting_reviews(self, r_longboarding):
        fake_review_title = 'Test Review'

        r_longboarding.post_review(fake_review_title)

        r_longboarding.reddit.submit.assert_called_with(
            'longboarding',
            fake_review_title,
            text=r_longboarding.review_text(fake_review_title)
        )

    def test_credentials(self, r_longboarding):
        set_test_credentials()

        assert r_longboarding.credentials == TEST_CREDENTIALS

    def test_review_text(self, r_longboarding):
        assert r_longboarding.review_text('Potato') == 'This is a test post. Potato'
