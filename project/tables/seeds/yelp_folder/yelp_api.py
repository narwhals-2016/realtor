import json
from math import log
from pprint import pprint

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


"""
how auth and client objects are made:

auth = Oauth1Authenticator(
    consumer_key=YOUR_CONSUMER_KEY,
    consumer_secret=YOUR_CONSUMER_SECRET,
    token=YOUR_TOKEN,
    token_secret=YOUR_TOKEN_SECRET
)

client = Client(auth)
"""

# read API keys
def get(location, term):
	params = {
		'location': location,
		'term': term,
	}
	with open('yelp_config_secret.json') as cred:
	    creds = json.load(cred)
	    auth = Oauth1Authenticator(**creds)
	    client = Client(auth)
	    response = client.search(**params)
	    total_results = response.total
	    businesses = [business for business in response.businesses]
	    average_rating = sum([business.rating for business in businesses])/len(businesses)
	    return {
	    	'total': total_results,
	    	'selected_businesses_count': len(businesses),
	    	'average_rating': average_rating,
	    }



# this works where dictionary values are zip code strings
def run(nb_dict, term):
	responses = {}
	for nb in nb_dict:
		loc = nb + "," + nb_dict[nb]
		response = get(location=loc,term=term)
		responses[nb] = (
			response['total'], 
			response['selected_businesses_count'], 
			response['average_rating']
		)
	return responses

# do yelp call for array of zip codes; business totals are added for each nb,
# while rating is averaged
# dictionary in mappings.py used
def run_list(nb_dict, term):
	responses = {}
	for nb in nb_dict:
		zip_code_container = []
		for zip_code in nb_dict[nb]:
			response = get(location=nb + "," + zip_code, term=term)
			zip_code_container.append((
				response['total'], 
				response['selected_businesses_count'], 
				response['average_rating']
			))
		responses[nb] = (
			sum([tup[0] for tup in zip_code_container]),
			sum([tup[1] for tup in zip_code_container]),
			sum([tup[2] for tup in zip_code_container])/len(zip_code_container),
		)
	return responses


def get_scores(my_dict):
	results = {}
	for key in my_dict:
		values = my_dict[key]
		# score equals log of total businesses times average rating. total variation is enormous, so log scales it down. score is combination of total and rating
		score = round(log(values[0])*values[2],2)
		results[key] = score
	return results

def sort_dict(my_dict):
	return sorted(my_dict.items(), key = lambda x:x[1])

"""
4/20/16 Goal: feed every nb and zip into api for 'food' and 'restaurant', and get total responses.
get average rating too for the selected 20.
save businesses for bonus goal
bonus goal: see if anything worthwhile can be done with businesses, like categories, neighborhoods, or zip codes

"""


