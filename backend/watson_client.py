from configs import watson_conf
import json
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

conf = watson_conf.cred

def get_insights(payload):
	personality_insights = PersonalityInsights(username=conf["username"], password=conf["password"])
	insights = personality_insights.profile(text=payload)
	# TODO retrive insights