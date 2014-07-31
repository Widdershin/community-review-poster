import autoposter

import pytest

from unittest.mock import MagicMock


@pytest.fixture
def r_longboarding():
    fake_reddit = MagicMock(autospec='praw.Reddit')
    api = autoposter.RLongboarding(reddit_api=lambda name: fake_reddit)
    return api


class TestRLongboarding(object):

    def test_posting_reviews(self, r_longboarding):
        fake_review_title = 'Test Review'

        r_longboarding.post_review(fake_review_title)

        r_longboarding.reddit.submit.assert_called_with(
            'longboarding',
            fake_review_title
        )
