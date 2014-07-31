import autoposter

from unittest.mock import Mock
import pytest


@pytest.fixture
def app():
    return autoposter.App()


class TestApp(object):
    def test_it_can_be_instantiated(self, app):
        assert isinstance(app, autoposter.App)

    def test_posting_top_review(self):
        pass


class TestPostingTopReview(object):

    def test_get_top_review(self, app):

        app.reviews.get_top_review = Mock()

        app.get_top_review()

        app.reviews.get_top_review.assert_called()
