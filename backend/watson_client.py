from configs import watson_conf
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights

conf = watson_conf.cred


def get_insights(payload):
	personality_insights = PersonalityInsights(username=conf["username"], password=conf["password"])

	with open(join(dirname(__file__), payload)) as personality_text:
		print(json.dumps(personality_insights.profile(text=personality_text.read())))