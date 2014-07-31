Responsibilities:

* When run, get the top suggested review from reviews.rlongboarding.com
* Post it on /r/longboarding
* Mark it as posted on reviews.rlongboarding.com


Components


Reviews - deals with reviews.rlongboarding.com
	get_top_review : Review
	mark_review_complete(id)


RLongboarding - deals with /r/longboarding stuff
	update_sidebar_review(review)
	post_review(review)


App - orchestrates other pieces
	post_top_review
		talks to reviews to get top review
		talks to RedditPoster to post it to reddit
		talks to reviews to mark it completed
		talks to rlongboard to update the link in the sidebar
		notify of failures


Technologies:

requests, PRAW
