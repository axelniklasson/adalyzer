import requests
import json


dummy = { "contentItems" : [
	{
		"userid" : "user1",
		"id" : "uuid1.1",
		"contenttype" : "text/plain",
		"language" : "en",
		"created" : 1393264847000,
		"content": "some text"
	},
	{
		"userid" : "user1",
		"id" : "uuid1.2",
		"contenttype" : "text/plain",
		"language" : "en",
		"created" : 1393263869000,
		"content": "even more"
	},
	{
		"userid" : "user2",
		"id" : "uuid2",
		"contenttype" : "text/plain",
		"language" : "en",
		"created" : 1394826985000,
		"content": "this is a different author"
	}
] }

conf = {}
execfile("backend/configs/watson_conf", conf)

def get_insights(payload):
	response = requests.post(conf["url"], auth=(conf["username"],
	                                            conf["password"]),
	                         headers={"Content-Type": "application/json", "Accept": "text/csv"},
	                         data = json.dumps(payload))
	return response.content