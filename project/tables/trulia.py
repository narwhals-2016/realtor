import requests
import json

from django.conf import settings




params ={
	'library': 'TruliaStats',
	'function': 'getZipCodeStats',
	'startDate': '2016-03-21',
	'endDate': '2016-04-01',
	'zipCode': '11201',
	# 'statType': 'traffic',
}



class TruliaAPI:
	def __init__(self, access_key):
		self.access_key = access_key

	def get(self, kwargs):
		URL = "http://api.trulia.com/webservices.php?"
		params = kwargs
		params.update({"apikey": self.access_key})
		return requests.get(URL, params=params)

api = TruliaAPI(settings.TRULIA_KEY)