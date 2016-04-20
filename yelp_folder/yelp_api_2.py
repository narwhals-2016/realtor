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
	    	'total': total_results,
	    	'selected_businesses_count': len(businesses),
	    	'average_rating': average_rating,
	    }



# def nb_check(result):
	# return [business.location.neighborhoods for business in result['businesses']]


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

"""
4/20/16 Goal: feed every nb and zip into api for 'food' and 'restaurant', and get total responses.
get average rating too for the selected 20.
save businesses for bonus goal
bonus goal: see if anything worthwhile can be done with businesses, like categories, neighborhoods, or zip codes

"""

# mapping from nb-zip/nb-zip.py 4/20/16
best_matches = {
	'Allerton-Pelham Gardens': '10312',
	"Annadale-Huguenot-Prince's Bay-Eltingville": '10312',
	'Arden Heights': 'MISSING',
	'Astoria': '11103',
	'Auburndale': '11358',
	'Baisley Park': '11434',
	'Bath Beach': '11214',
	'Battery Park City-Lower Manhattan': '10280',
	'Bay Ridge': '11209',
	'Bayside-Bayside Hills': '11361',
	'Bedford Park-Fordham North': '10458',
	'Bedford brooklyn': '11216',
	'Bellerose': '11426',
	'Belmont bronx': '10458',
	'Bensonhurst East': '11204',
	'Bensonhurst West': '11214',
	'Borough Park': '11219',
	'Breezy Point-Belle Harbor-Rockaway Park-Broad': '11697',
	'Briarwood-Jamaica Hills': '11435',
	'Brighton Beach': '11235',
	'Bronxdale': '10462',
	'Brooklyn Heights-Cobble Hill': '11201',
	'Brownsville': '11212',
	'Bushwick North': '11237',
	'Bushwick South': '11237',
	'Cambria Heights': '11411',
	'Canarsie': '11236',
	'Carroll Gardens-Columbia Street-Red Hook': '11231',
	'Central Harlem North-Polo Grounds': '10039',
	'Central Harlem South': '10026',
	'Charleston-Richmond Valley-Tottenville': '10307',
	'Chinatown': '10013',
	'Claremont-Bathgate': '10457',
	'Clinton Hill': '11205',
	'Co-Op City': '10475',
	'College Point': '11356',
	'Corona': '11368',
	'Crotona Park East': '10460',
	'Crown Heights North': '11225',
	'Crown Heights South': '11225',
	'Cypress Hills-City Line': '11208',
	'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': '11201',
	'Douglas Manor-Douglaston-Little Neck': '11362',
	'Dyker Heights': '11228',
	'East Concourse-Concourse Village': '10451',
	'East Elmhurst': '11369',
	'East Flatbush-Farragut': '11203',
	'East Flushing': '11354',
	'East Harlem North': '10037',
	'East Harlem South': '10029',
	'East New York': '11207',
	'East New York (Pennsylvania Ave)': '11207',
	'East Tremont': '10457',
	'East Village': '10009',
	'East Williamsburg': '11211',
	'Eastchester-Edenwald-Baychester': '10475',
	'Elmhurst': '11373',
	'Elmhurst-Maspeth': '11373',
	'Erasmus': '11226',
	'Far Rockaway-Bayswater': '11691',
	'Flatbush': '11226',
	'Flatlands': '11234',
	'Flushing': '11354',
	'Fordham South': '10458',
	'Forest Hills': '11375',
	'Fort Greene': '11205',
	'Fresh Meadows-Utopia': '11365',
	'Ft. Totten-Bay Terrace-Clearview': '11360',
	'Georgetown-Marine Park-Bergen Beach-Mill Basi': '11234',
	'Glen Oaks-Floral Park-New Hyde Park': '11040',
	'Glendale': '11385',
	'Gramercy': '10003',
	'Grasmere-Arrochar-Ft. Wadsworth': '10304',
	'Gravesend': '11223',
	'Great Kills': '10308',
	'Greenpoint': '11222',
	'Grymes Hill-Clifton-Fox Hills': '10301',
	'Hamilton Heights': '10031',
	'Hammels-Arverne-Edgemere': '11692',
	'Highbridge': '10452',
	'Hollis': '11423',
	'Homecrest': '11223',
	'Hudson Yards-Chelsea-Flat Iron-Union Square': '10011',
	'Hunters Point-Sunnyside-West Maspeth': '11104',
	'Hunts Point': '10474',
	'Jackson Heights': '11372',
	'Jamaica': '11432',
	'Jamaica Estates-Holliswood': '11423',
	'Kensington-Ocean Parkway': '11218',
	'Kew Gardens': '11415',
	'Kew Gardens Hills': '11415',
	'Kingsbridge Heights': '10463',
	'Laurelton': '11413',
	'Lenox Hill-Roosevelt Island': '10065',
	'Lincoln Square': '10023',
	'Lindenwood-Howard Beach': '11414',
	'Longwood': '10455',
	'Lower East Side': '10002',
	'Madison brookl': '11229',
	'Manhattanville': '10027',
	'Marble Hill-Inwood': '10034',
	"Mariner's Harbor-Arlington-Port Ivory-Granite": '10303',
	'Maspeth': '11378',
	'Melrose South-Mott Haven North': '10451',
	'Middle Village': '11379',
	'Midtown-Midtown South': '10019',
	'Midwood': '11230',
	'Morningside Heights': '10027',
	'Morrisania-Melrose': '10456',
	'Mott Haven-Port Morris': '10454',
	'Mount Hope': '10003',
	'Murray Hill': '10016',
	'Murray Hill-Kips Bay': '10016',
	'New Brighton-Silver Lake': '10301',
	'New Dorp-Midland Beach': '10306',
	'New Springville-Bloomfield-Travis': '10314',
	'North Corona': '11368',
	'North Riverdale-Fieldston-Riverdale': '10471',
	'North Side-South Side': 'MISSING',
	'Norwood': '10467',
	'Oakland Gardens': '11364',
	'Oakwood-Oakwood Beach': '10306',
	'Ocean Hill': '11233',
	'Ocean Parkway South': '11230',
	'Old Astoria': '11102',
	'Old Town-Dongan Hills-South Beach': '10305',
	'Ozone Park': '11417',
	'Parkchester': '10462',
	'Pelham Bay-Country Club-City Island': '10464',
	'Pelham Parkway': '10062',
	'Pomonok-Flushing Heights-Hillcrest': '11354',
	'Port Richmond': '10302',
	'Prospect Heights': '11238',
	'Prospect Lefferts Gardens-Wingate': '11225',
	'Queens Village': '11428',
	'Queensboro Hill queens': '11355',
	'Queensbridge-Ravenswood-Long Island City': '11106',
	'Rego Park': '11374',
	'Richmond Hill': '11418',
	'Ridgewood': '11385',
	'Rikers Island': 'MISSING',
	'Rosedale': '11422',
	'Rossville-Woodrow': '10309',
	'Rugby-Remsen Village': '11203',
	'Schuylerville-Throgs Neck-Edgewater Park': '10465',
	'Seagate-Coney Island': '11224',
	'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': '11235',
	'SoHo-TriBeCa-Civic Center-Little Italy': '10013',
	'Soundview-Bruckner': '10472',
	'Soundview-Castle Hill-Clason Point-Harding Pa': '10472',
	'South Jamaica': '11433',
	'South Ozone Park': '11436',
	'Springfield Gardens North': '11413',
	'Springfield Gardens South-Brookville': '11413',
	'Spuyten Duyvil-Kingsbridge': '10463',
	'St. Albans': '11412',
	'Stapleton-Rosebank': '10305',
	'Starrett City': '11239',
	'Steinway': '11105',
	'Stuyvesant Heights nyc': '11233',
	'Stuyvesant Town-Cooper Village': '10009',
	'Sunset Park East': '11220',
	'Sunset Park West': '11220',
	'Todt Hill-Emerson Hill-Heartland Village-Ligh': '10304',
	'Turtle Bay-East Midtown': '10022',
	'University Heights-Morris Heights': '10453',
	'Upper East Side-Carnegie Hill': '10075',
	'Upper West Side': '10024',
	'Van Cortlandt Village': '10468',
	'Van Nest-Morris Park-Westchester Square': '10462',
	'Washington Heights North': '10033',
	'Washington Heights South': '10033',
	'West Brighton': '10310',
	'West Concourse': '10451',
	'West Farms-Bronx River': '10460',
	'West New Brighton-New Brighton-St. George': '10310',
	'West Village': '10014',
	'Westchester-Unionport': '10461',
	'Westerleigh': '10314',
	'Whitestone': '11357',
	'Williamsbridge-Olinville': '10467',
	'Williamsburg': '11211',
	'Windsor Terrace': '11215',
	'Woodhaven': '11421',
	'Woodlawn-Wakefield': '10466',
	'Woodside': '11377',
	'Yorkville nyc': '10128',
	"hell's kitchen": '10019',
}
