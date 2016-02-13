from twitter import *
import numpy as np

conf = {}
execfile("backend/configs/twitter_conf", conf)
twitter = Twitter(auth=OAuth(conf["a_key"], conf["a_secret"], conf["c_key"], conf["c_secret"]))

def get_tweets(keyword, geocode, nmbr_of_tweets=100, lang="sv"):
	res_arr = np.empty(nmbr_of_tweets)
	count = 0
	for i in range(0, nmbr_of_tweets % 100):
		if nmbr_of_tweets <= 100:
			count += nmbr_of_tweets
			query = twitter.search.tweets(q=keyword, geocode=geocode, count=nmbr_of_tweets, lang=lang)
		else:
			count += 100
			query = twitter.search.tweets(q=keyword, geocode=geocode, count=100, lang=lang)

		for j in range(0, res_arr.size):
			res_arr[i] = query["statuses"]["text"]

	return res_arr