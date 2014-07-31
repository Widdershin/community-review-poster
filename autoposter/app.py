from autoposter.reviews import Reviews


class App(object):
    def __init__(self):
        self.reviews = Reviews()

    def get_top_review(self):
        return self.reviews.get_top_review()
