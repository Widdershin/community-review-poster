
import autoposter

import pytest
from httmock import urlmatch, HTTMock


@urlmatch(netloc='http://reviews.rlongboarding.com/reviews$')
def reviews_mock(url, request):
    response = {
        "status_code": 200,
        "headers": {'content-type': 'application/json'},
        "content": {
            "reviews":
            [
                {"id": 4, "name": "Caliber II's", "score": 33},
                {"id": 1, "name": "Earthwing NLS", "score": 32}
            ]
        }
    }
    return response


@pytest.fixture()
def reviews():
    return autoposter.Reviews()


class TestReviews(object):
    def test_getting_top_review(self, reviews):
        with HTTMock(reviews_mock):
            review = reviews.get_top_review()

        assert review.name == "Caliber II's"
