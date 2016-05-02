"""
MUST PIP3 INSTALL TRULIA. DETAILS: https://pypi.python.org/pypi/trulia/
"""

from statistics import mean
import trulia.stats
from django.conf import settings

# enter zip_code and dates as strings
# date format: "YYYY-MM-DD"
def zip_stats(zip_code, start_date, end_date):
	response = trulia.stats.TruliaStats(settings.TRULIA_KEY).get_zip_code_stats(
		zip_code=zip_code, start_date=start_date, end_date=end_date,
	)
	try:
		all_properties_median_price = int(response['listingStats']['listingStat'][0]['listingPrice']['subcategory'][0]['medianListingPrice'])	
		print(zip_code, all_properties_median_price)
	except KeyError:
		try:
			all_properties_median_price = int(response['listingStats']['listingStat']['listingPrice']['subcategory'][0]['medianListingPrice'])
		except TypeError:	
			print('response did not play nice: ', zip_code)
			all_properties_median_price = -1
	return all_properties_median_price

# nb_zip
# all_zips(nb_zip, '2016-04-01','2016-04-01')
def all_zips(mapping, start_date, end_date):
	median_dict = {}
	for nb in mapping:
		print(nb)
		median_holder = []
		for zip_code in mapping[nb]:
			if zip_code != 'MISSING':
				print(zip_code)
				zip_median = zip_stats(
					zip_code=zip_code,
					start_date=start_date,
					end_date=end_date
					)
				median_holder.append(zip_median)
			else:
				print(nb, zip_code, '**********************************')
		median_dict[nb] = mean(median_holder)
	return median_dict 




# USE PYTHON PACKAGE TRULIA
# can get averagelistingprice, medianlistingprice, for...
# all properties: ['subcategory'][0]
# 1 bedroom: ['subcategory'][1]
                                 # first week is zero index
# response['listingStats']['listingStat'][0]['listingPrice']['subcategory'][0]





# NO LONGER NEED
# import requests
# import json

# params ={
# 	'library': 'TruliaStats',
# 	'function': 'getZipCodeStats',
# 	'startDate': '2016-03-21',
# 	'endDate': '2016-04-01',
# 	'zipCode': '11201',
# 	# 'statType': 'traffic',
# }


# # DON'T USE BELOW; GETS XML RESPONSE, USE PYTHON PACKAGE
# class TruliaAPI:
# 	def __init__(self, access_key):
# 		self.access_key = access_key

# 	def get(self, kwargs):
# 		URL = "http://api.trulia.com/webservices.php?"
# 		params = kwargs
# 		params.update({"apikey": self.access_key})
# 		return requests.get(URL, params=params)

# api = TruliaAPI(settings.TRULIA_KEY)