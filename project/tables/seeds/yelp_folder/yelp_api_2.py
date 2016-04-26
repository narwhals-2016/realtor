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
	    	'total': total_results,
	    	'selected_businesses_count': len(businesses),
	    	'average_rating': average_rating,
	    }



# def nb_check(result):
	# return [business.location.neighborhoods for business in result['businesses']]

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
dict_of_arrays = {'Breezy Point-Belle Harbor-Rockaway Park-Broad': ['11697'], 'East New York': ['11207'], 'Bushwick North': ['11237'], 'Elmhurst': ['11373'], 'South Ozone Park': ['11436'], 'Arden Heights': ['MISSING'], 'Central Harlem North-Polo Grounds': ['10039'], 'Westchester-Unionport': ['10461'], 'Rosedale': ['11422'], 'Schuylerville-Throgs Neck-Edgewater Park': ['10465'], 'New Brighton-Silver Lake': ['10301'], 'Crotona Park East': ['10460'], 'Prospect Heights': ['11238'], 'Morningside Heights': ['10027'], 'Bushwick South': ['11237'], 'Port Richmond': ['10302'], "Mariner's Harbor-Arlington-Port Ivory-Granite": ['10303'], 'Kew Gardens': ['11415'], 'Great Kills': ['10308'], 'East Elmhurst': ['11369'], 'Melrose South-Mott Haven North': ['10451'], 'Central Harlem South': ['10026'], 'Corona': ['11368'], 'West Village': ['10014', '10012'], 'Douglas Manor-Douglaston-Little Neck': ['11362'], 'Dyker Heights': ['11228'], 'Astoria': ['11103'], 'Belmont bronx': ['10458'], 'East Harlem North': ['10037'], 'Spuyten Duyvil-Kingsbridge': ['10463'], 'Longwood': ['10455'], 'Bensonhurst West': ['11214'], 'North Side-South Side': ['MISSING'], 'Sunset Park West': ['11220'], 'Battery Park City-Lower Manhattan': ['10280', '10038', '10004', '10006', '10005'], "Annadale-Huguenot-Prince's Bay-Eltingville": ['10312'], 'Fort Greene': ['11205'], 'Jackson Heights': ['11372'], 'Sunset Park East': ['11220'], 'Auburndale': ['11358'], 'West Farms-Bronx River': ['10460'], 'Greenpoint': ['11222'], 'New Dorp-Midland Beach': ['10306'], 'Oakland Gardens': ['11364'], 'College Point': ['11356'], 'Hunters Point-Sunnyside-West Maspeth': ['11104'], 'Jamaica': ['11432'], 'Chinatown': ['10013'], 'Flatbush': ['11226'], 'Madison brookl': ['11229'], 'Allerton-Pelham Gardens': ['10312'], 'Bay Ridge': ['11209'], 'Queensboro Hill queens': ['11355'], 'Ocean Hill': ['11233'], 'Clinton': ['10036', '10019', '10018'], 'Brighton Beach': ['11235'], 'Eastchester-Edenwald-Baychester': ['10475'], 'Williamsbridge-Olinville': ['10467', '11249'], 'Woodside': ['11377'], 'Bath Beach': ['11214'], 'Briarwood-Jamaica Hills': ['11435'], 'Kensington-Ocean Parkway': ['11218'], 'West Concourse': ['10451'], 'Van Cortlandt Village': ['10468'], 'Stapleton-Rosebank': ['10305'], 'North Riverdale-Fieldston-Riverdale': ['10471'], 'Ridgewood': ['11385'], 'Cypress Hills-City Line': ['11208'], 'Gramercy': ['10003'], 'Ft. Totten-Bay Terrace-Clearview': ['11360'], 'Pelham Parkway': ['10062'], 'Maspeth': ['11378'], 'Hamilton Heights': ['10031'], 'Homecrest': ['11223'], 'Mott Haven-Port Morris': ['10454'], 'Richmond Hill': ['11418'], 'Queens Village': ['11428'], 'Canarsie': ['11236'], 'Cambria Heights': ['11411'], 'Bensonhurst East': ['11204'], 'Rossville-Woodrow': ['10309'], 'East Harlem South': ['10029'], 'Far Rockaway-Bayswater': ['11691'], 'Charleston-Richmond Valley-Tottenville': ['10307'], 'Lenox Hill-Roosevelt Island': ['10065'], 'Fresh Meadows-Utopia': ['11365'], 'Forest Hills': ['11375'], 'Lower East Side': ['10002'], 'West Brighton': ['10310'], 'Lindenwood-Howard Beach': ['11414'], 'Carroll Gardens-Columbia Street-Red Hook': ['11231'], 'Ozone Park': ['11417'], 'Bronxdale': ['10462'], 'Crown Heights South': ['11225'], 'Co-Op City': ['10475'], 'Bedford brooklyn': ['11216'], 'Glen Oaks-Floral Park-New Hyde Park': ['11040'], 'Baisley Park': ['11434'], 'Queensbridge-Ravenswood-Long Island City': ['11106', '11101'], 'Kew Gardens Hills': ['11415'], 'Seagate-Coney Island': ['11224'], 'Pomonok-Flushing Heights-Hillcrest': ['11354', '11206'], 'Bedford Park-Fordham North': ['10458'], 'Van Nest-Morris Park-Westchester Square': ['10462'], 'Flushing': ['11354'], 'Oakwood-Oakwood Beach': ['10306'], 'Soundview-Bruckner': ['10472'], 'Stuyvesant Heights nyc': ['11233'], 'Washington Heights South': ['10033'], 'Glendale': ['11385'], 'University Heights-Morris Heights': ['10453'], 'Old Astoria': ['11102'], 'Todt Hill-Emerson Hill-Heartland Village-Ligh': ['10304'], 'St. Albans': ['11412'], 'Parkchester': ['10462'], 'Washington Heights North': ['10040', '10032', '10033'], 'Elmhurst-Maspeth': ['11373'], 'Hudson Yards-Chelsea-Flat Iron-Union Square': ['10011', '10001'], 'Marble Hill-Inwood': ['10034'], 'Woodhaven': ['11421'], 'Stuyvesant Town-Cooper Village': ['10009', '10010'], 'Springfield Gardens North': ['11413'], 'Rego Park': ['11374'], "hell's kitchen": ['10019'], 'New Springville-Bloomfield-Travis': ['10314'], 'Hollis': ['11423'], 'Springfield Gardens South-Brookville': ['11413'], 'Brooklyn Heights-Cobble Hill': ['11201'], 'Turtle Bay-East Midtown': ['10022'], 'Manhattanville': ['10027'], 'Lincoln Square': ['10023'], 'Murray Hill': ['10016'], 'Flatlands': ['11234'], 'East Concourse-Concourse Village': ['10451'], 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': ['11201', '11217'], 'Pelham Bay-Country Club-City Island': ['10464'], 'North Corona': ['11368'], 'Gravesend': ['11223'], 'Morrisania-Melrose': ['10456'], 'Old Town-Dongan Hills-South Beach': ['10305'], 'Bellerose': ['11426'], 'Mount Hope': ['10003'], 'East New York (Pennsylvania Ave)': ['11207'], 'South Jamaica': ['11433'], 'Brownsville': ['11212'], 'Grymes Hill-Clifton-Fox Hills': ['10301'], 'Windsor Terrace': ['11215'], 'Borough Park': ['11219'], 'Erasmus': ['11226'], 'Kingsbridge Heights': ['10463'], 'Highbridge': ['10452'], 'Midwood': ['11230'], 'Woodlawn-Wakefield': ['10466'], 'Whitestone': ['11357'], 'West New Brighton-New Brighton-St. George': ['10310'], 'Middle Village': ['11379'], 'East Flushing': ['11354'], 'Hunts Point': ['10474'], 'Crown Heights North': ['11225'], 'Hammels-Arverne-Edgemere': ['11692'], 'SoHo-TriBeCa-Civic Center-Little Italy': ['10013', '10007'], 'Midtown-Midtown South': ['10019'], 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': ['11235'], 'Soundview-Castle Hill-Clason Point-Harding Pa': ['10472'], 'East Tremont': ['10457'], 'Laurelton': ['11413'], 'Murray Hill-Kips Bay': ['10016'], 'Rikers Island': ['MISSING'], 'Starrett City': ['11239'], 'Bayside-Bayside Hills': ['11361'], 'Ocean Parkway South': ['11230'], 'Norwood': ['10467'], 'Claremont-Bathgate': ['10457'], 'Rugby-Remsen Village': ['11203'], 'Prospect Lefferts Gardens-Wingate': ['11225'], 'Jamaica Estates-Holliswood': ['11423'], 'Fordham South': ['10458'], 'East Williamsburg': ['11211'], 'Clinton Hill': ['11205'], 'Yorkville nyc': ['10128'], 'Upper West Side': ['10024', '10025'], 'Steinway': ['11105'], 'East Village': ['10009'], 'Georgetown-Marine Park-Bergen Beach-Mill Basi': ['11234'], 'East Flatbush-Farragut': ['11203'], 'Grasmere-Arrochar-Ft. Wadsworth': ['10304'], 'Westerleigh': ['10314'], 'Williamsburg': ['11211'], 'Upper East Side-Carnegie Hill': ['10128', '10028', '10075', '10021']}

