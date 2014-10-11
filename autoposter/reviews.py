from collections import namedtuple
import os
import requests
from operator import attrgetter

REVIEWS_URL = 'http://reviews.rlongboarding.com/reviews'

class Review(namedtuple('Review', ['name', 'id', 'score', 'suggested_by', 'submitted'])):
    def mark_as_posted(self):
        response = requests.patch(REVIEWS_URL, data=self.posted_args)

        response.raise_for_status()

    @property
    def posted_args(self):
        return {
            "id": self.id,
            "submitted": "true",
            "key": os.environ["AUTOPOSTER_KEY"],
        }


class Reviews(object):
    """Python API for reviews.rlongboarding.com"""
    def __init__(self, endpoint=REVIEWS_URL):
        self.endpoint = endpoint

    def get_top_review(self):
        response = requests.get(self.endpoint)

        return self._top_review_from_json(response.json())

    def _top_review_from_json(self, json):
        reviews = [Review(**review_json) for review_json in json['reviews']]
        unsubmitted_reviews = [review for review in reviews if not review.submitted]
        return self._top_review(unsubmitted_reviews)

    def _top_review(self, reviews):
        return sorted(reviews, key=attrgetter('score'), reverse=True)[0]
