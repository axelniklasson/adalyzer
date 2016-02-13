import twitter_client
import watson_client


class Personality:

	def __init__(self):
		self.personality = None

	def get_insights(self, persona):
		tweets = []
		for p in persona:
			if persona[p] > 0:
				tweet = twitter_client.get_tweets(p, persona[p]*100)
				tweets.append(tweet)

		watson_data = watson_client.get_insights(tweets)

		self.personality = watson_data

	def get_personality(self):
		return self.personality