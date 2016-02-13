import twitter_client
import watson_client


def get_insights(persona):
	tweets = []
	for p in persona:
		if persona[p] > 0:
			tweet = twitter_client.get_tweets(p, persona[p]*100)
			tweets.append(tweet)

	return watson_client.get_insights(tweets)