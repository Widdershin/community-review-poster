from collections import namedtuple
import requests
from operator import attrgetter


class Review(namedtuple('Review', ['name', 'id', 'score'])):
    pass


class Reviews(object):
    def __init__(self, endpoint='http://reviews.rlongboarding.com/reviews'):
        self.endpoint = endpoint

    def get_top_review(self):
        response = requests.get(self.endpoint)

        return self._top_review_from_json(response.json())

    def _top_review_from_json(self, json):
        reviews = [Review(**review_json) for review_json in json['reviews']]
        return self._top_review(reviews)

    def _top_review(self, reviews):
        return sorted(reviews, key=attrgetter('score'), reverse=True)[0]
