from autoposter.reviews import Reviews
from autoposter.r_longboarding import RLongboarding

class App(object):
    def __init__(self):
        self.reviews = Reviews()

    def get_top_review(self):
        return self.reviews.get_top_review()

    def post_top_review(self):
        review = self.get_top_review()
        subreddit = RLongboarding()
        subreddit.login()

        subreddit.post_review(
            "Community Review: {name}".format(name=review.name),
            self.post_text(review)
        )

        review.mark_as_posted()

    def post_text(self, review):
        with open('autoposter/data/review_template.md') as review_file:
            return review_file.read().format(review=review)

if __name__ == '__main__':
    App().post_top_review()

