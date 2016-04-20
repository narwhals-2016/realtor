import json

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
neighborhoods = ["Gravesend","Stapleton-Rosebank","Grasmere-Arrochar-Ft. Wadsworth","Grymes Hill-Clifton-Fox Hills","Old Town-Dongan Hills-South Beach","New Brighton-Silver Lake","New Dorp-Midland Beach","West New Brighton-New Brighton-St. George","Oakwood-Oakwood Beach","Westerleigh","Port Richmond","Borough Park","Great Kills","Todt Hill-Emerson Hill-Heartland Village-Ligh","Mariner's Harbor-Arlington-Port Ivory-Granite","Arden Heights","New Springville-Bloomfield-Travis","Rossville-Woodrow","Annadale-Huguenot-Prince's Bay-Eltingville","Charleston-Richmond Valley-Tottenville","Rosedale","Far Rockaway-Bayswater","Bensonhurst West","Springfield Gardens North","Springfield Gardens South-Brookville","Hammels-Arverne-Edgemere","Lindenwood-Howard Beach","Starrett City","East New York (Pennsylvania Ave)","East New York","Canarsie","Brownsville","Rugby-Remsen Village","Seagate-Coney Island","Breezy Point-Belle Harbor-Rockaway Park-Broad","Georgetown-Marine Park-Bergen Beach-Mill Basi","Flatlands","East Flatbush-Farragut","Madison brookl","Erasmus","Sheepshead Bay-Gerritsen Beach-Manhattan Beac","Crown Heights South","Prospect Lefferts Gardens-Wingate","Brighton Beach","Sunset Park East","Midwood","Homecrest","Flatbush","Ocean Parkway South","West Brighton","Kensington-Ocean Parkway","Windsor Terrace","Glen Oaks-Floral Park-New Hyde Park","Bellerose","Cambria Heights","Bath Beach","Douglas Manor-Douglaston-Little Neck","Queens Village","Laurelton","Oakland Gardens","Hollis","St. Albans","Jamaica Estates-Holliswood","Bayside-Bayside Hills","Fresh Meadows-Utopia","Auburndale","Dyker Heights","Ft. Totten-Bay Terrace-Clearview","Baisley Park","South Jamaica","Pomonok-Flushing Heights-Hillcrest","Jamaica","East Flushing","Briarwood-Jamaica Hills","Murray Hill","Kew Gardens Hills","Queensboro Hill queens","Sunset Park West","Flushing","South Ozone Park","Whitestone","Kew Gardens","Richmond Hill","Stuyvesant Town-Cooper Village","East Village","Greenpoint","Maspeth","Rego Park","Bay Ridge","SoHo-TriBeCa-Civic Center-Little Italy","Chinatown","Bensonhurst East","Forest Hills","Bushwick North","Fort Greene","Bedford brooklyn","Woodhaven","DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H","Bushwick South","Clinton Hill","Stuyvesant Heights nyc","Cypress Hills-City Line","Prospect Heights","Lower East Side","Ocean Hill","Ozone Park","Carroll Gardens-Columbia Street-Red Hook","Crown Heights North","Morningside Heights","Central Harlem South","Mott Haven-Port Morris","East Harlem North","Rikers Island","East Harlem South","North Side-South Side","Upper West Side","Yorkville nyc","Lincoln Square","Steinway","College Point","Old Astoria","Upper East Side-Carnegie Hill","East Elmhurst","hell's kitchen","Astoria","East Williamsburg","Lenox Hill-Roosevelt Island","Queensbridge-Ravenswood-Long Island City","Jackson Heights","North Corona","Midtown-Midtown South","Turtle Bay-East Midtown","Woodside","Hudson Yards-Chelsea-Flat Iron-Union Square","Corona","Murray Hill-Kips Bay","Williamsburg","Elmhurst-Maspeth","Gramercy","Elmhurst","West Village","Hunters Point-Sunnyside-West Maspeth","Pelham Bay-Country Club-City Island","Schuylerville-Throgs Neck-Edgewater Park","Co-Op City","Eastchester-Edenwald-Baychester","Westchester-Unionport","Battery Park City-Lower Manhattan","Allerton-Pelham Gardens","Parkchester","Pelham Parkway","Williamsbridge-Olinville","Bronxdale","Van Nest-Morris Park-Westchester Square","Woodlawn-Wakefield","West Farms-Bronx River","Soundview-Castle Hill-Clason Point-Harding Pa","Soundview-Bruckner","Glendale","Norwood","Belmont bronx","East Tremont","Crotona Park East","Bedford Park-Fordham North","Hunts Point","Longwood","Fordham South","Van Cortlandt Village","Claremont-Bathgate","Ridgewood","Kingsbridge Heights","Morrisania-Melrose","Mount Hope","North Riverdale-Fieldston-Riverdale","Spuyten Duyvil-Kingsbridge","Melrose South-Mott Haven North","East Concourse-Concourse Village","University Heights-Morris Heights","Marble Hill-Inwood","West Concourse","Brooklyn Heights-Cobble Hill","Highbridge","Washington Heights North","Washington Heights South","Central Harlem North-Polo Grounds","Hamilton Heights","Manhattanville","Middle Village"]

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
	    	'response': response,
	    	'total': total_results,
	    	'businesses': businesses,
	    	'selected_businesses_count': len(businesses),
	    	'average_rating': average_rating,
	    }

def nb_check(result):
	return [business.location.neighborhoods for business in result['businesses']]


# def run(nb_list, term):
# 	results = {}
	# for nb in nb_list:
	# 	response = get(location=nb,term=term)
	# 	results[nb] = response

"""
4/20/16 Goal: feed every nb and zip into api for 'food' and 'restaurant', and get total responses.
get average rating too for the selected 20.
save businesses for bonus goal
bonus goal: see if anything worthwhile can be done with businesses, like categories, neighborhoods, or zip codes

"""
