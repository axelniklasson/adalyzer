from twitter import *
from configs import twitter_conf


conf = twitter_conf
twitter = Twitter(auth=OAuth(conf.a_key, conf.a_secret, conf.c_key, conf.c_secret))


def get_tweets(keyword, nmbr_of_tweets=100, lang="sv"):
	res_arr = []
	no_tweets = nmbr_of_tweets
	prev = 0
	for i in range(0, int(nmbr_of_tweets / 100)):
		if no_tweets <= 100:
			query = twitter.search.tweets(q=keyword, count=no_tweets, lang=lang)
		else:
			query = twitter.search.tweets(q=keyword, count=100, lang=lang)
			no_tweets -= 100
		for j in range(prev, len(query["statuses"])):
			res_arr.append(query["statuses"][j]["text"])
		prev += len(query["statuses"])

	return res_arr