import pandas as pd
from pprint import pprint
from math import log

def rd_csv(filepath):
	print('IN RD_CSV')
	df = pd.read_csv(filepath)
	# filter for nyc only
	return df[df['Agency Zone Office Name'] == 'New York City']


def five_digits(series):
	print('IN FIVE_DIGITS')
	f = lambda x: x[:5]
	# if parameter is dataframe object use applymap
	return series.apply(f)

# USE df.value_counts() to get 
# Series.to_dict() returns dictionary
"""
goal: get zip code count for all rows
"""
def get_zip_count(series):
	print('IN GET_ZIP_COUNT')
	counts = series.value_counts()
	count_dict = counts.to_dict()
	return count_dict

# nb_dict comes from mappings.py
def nb_count(nb_dict, zip_count):
	nb_count = {}
	nb_found = 0
	# iterate over every zip code in zip count
	for zip_key in zip_count:
		# check if zip code occurs in multiple neighborhoods, so must check every neighborhood
		for nb in nb_dict:
			# if zip code in in particular neighborhood we're checking
			if zip_key in nb_dict[nb]:
				# if nb already in nb_count
				print('zip found in nb: ', nb, ' - ', zip_key)
				nb_found += 1
				if nb in nb_count:
					# add to new count
					print('key exists, adding to count', nb)
					nb_count[nb] += zip_count[zip_key]
				else:
					# add nb to nb_count keys if not there
					print('adding key', nb)
					nb_count[nb] = zip_count[zip_key]
	return nb_count

def sort_dict(my_dict):
	return sorted(my_dict.items(), key = lambda x:x[1])

def get_scores(my_dict):
	results = {}
	for key in my_dict:
		# score equals log of total businesses times average rating. total variation is enormous, so log scales it down. score is combination of total and rating
		score = round(log(my_dict[key]),2)
		results[key] = score
	return results


# pass nb_zip from mappings.py as nb_dict
# liquor_filepath = 'tables/seeds/liquor/Licenses.csv'
def run_liquor(liquor_filepath, nb_dict):
	liquor_df = rd_csv(liquor_filepath)
	# zip_df = df['Zip'] # gets series of zip codes
	zip_df = liquor_df['Zip']
	zips = five_digits(zip_df)
	zip_count = get_zip_count(zips)
	nb_count(nb_dict, zip_count)
	return get_scores(nb_count)

# run_liquor() nb liquor count 4/28/16
logged_liquor = {'Maspeth': 4.43, 'Dyker Heights': 4.2, 'Bushwick South': 5.35, 'South Jamaica': 3.71, 'Jamaica Estates-Holliswood': 3.4, 'East Flushing': 5.44, 'East New York (Pennsylvania Ave)': 5.21, 'Bronxdale': 4.78, 'Grasmere-Arrochar-Ft. Wadsworth': 4.17, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 6.11, 'Madison': 4.74, 'Williamsbridge-Olinville': 5.27, 'Flatlands': 4.82, 'Rosedale': 3.3, 'Kew Gardens Hills': 3.43, 'Queens Village': 3.37, 'Ozone Park': 4.06, 'Hamilton Heights': 4.61, 'Old Astoria': 4.43, 'Bushwick North': 5.35, 'Old Town-Dongan Hills-South Beach': 4.52, 'Grymes Hill-Clifton-Fox Hills': 4.51, 'Springfield Gardens South-Brookville': 3.5, 'Lenox Hill-Roosevelt Island': 4.38, 'Woodlawn-Wakefield': 4.2, 'Crown Heights North': 4.56, 'Longwood': 4.5, 'Windsor Terrace': 5.73, 'Hunts Point': 3.56, 'Murray Hill': 5.86, 'Bedford': 4.84, 'Bedford Park-Fordham North': 5.12, 'Morningside Heights': 4.76, 'Murray Hill-Kips Bay': 5.86, 'West New Brighton-New Brighton-St. George': 3.97, 'Prospect Heights': 5.41, 'Astoria': 5.17, 'Oakwood-Oakwood Beach': 4.41, 'Morrisania-Melrose': 4.78, 'Westerleigh': 4.84, 'Oakland Gardens': 3.56, 'Belmont': 5.12, 'Rugby-Remsen Village': 4.74, 'Seagate-Coney Island': 4.39, 'Westchester-Unionport': 4.88, 'Borough Park': 4.61, 'New Dorp-Midland Beach': 4.41, 'Bensonhurst West': 5.02, 'Co-Op City': 3.58, 'Woodhaven': 4.25, 'Hunters Point-Sunnyside-West Maspeth': 4.53, 'Middle Village': 3.87, 'Ocean Hill': 4.53, 'Corona': 5.66, 'East Flatbush-Farragut': 4.74, 'Midwood': 4.38, 'Glendale': 5.63, 'Bay Ridge': 5.35, 'Manhattanville': 4.76, 'Bayside-Bayside Hills': 4.62, 'Parkchester': 4.78, 'East Williamsburg': 6.17, 'Melrose South-Mott Haven North': 4.61, 'Forest Hills': 5.02, 'Rossville-Woodrow': 4.13, 'Stuyvesant Town-Cooper Village': 6.21, 'University Heights-Morris Heights': 4.84, 'West Concourse': 4.61, 'Great Kills': 3.95, 'Cypress Hills-City Line': 5.12, 'Fresh Meadows-Utopia': 3.53, 'Upper West Side': 5.94, 'Mount Hope': 6.29, 'Richmond Hill': 4.52, 'Clinton Hill': 4.88, 'Ridgewood': 5.63, 'Brownsville': 4.78, 'New Springville-Bloomfield-Travis': 4.84, 'Kew Gardens': 3.43, 'Central Harlem North-Polo Grounds': 3.18, 'Hammels-Arverne-Edgemere': 2.08, 'Queensbridge-Ravenswood-Long Island City': 5.98, 'East Tremont': 4.88, 'Port Richmond': 4.14, 'Yorkville': 5.06, 'Steinway': 4.84, 'Brooklyn Heights-Cobble Hill': 5.55, 'Battery Park City-Lower Manhattan': 5.53, 'North Riverdale-Fieldston-Riverdale': 3.47, 'Chinatown': 5.81, 'Glen Oaks-Floral Park-New Hyde Park': 4.61, 'West Village': 6.57, 'South Ozone Park': 3.14, 'Crotona Park East': 4.48, 'Gramercy': 6.29, 'Erasmus': 5.03, 'Gravesend': 5.1, 'Bellerose': 3.09, 'Bath Beach': 5.02, 'Elmhurst-Maspeth': 5.05, 'East New York': 5.21, 'Laurelton': 3.5, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 6.59, 'Brighton Beach': 5.19, 'Jamaica': 4.57, 'West Farms-Bronx River': 4.48, 'Greenpoint': 5.44, 'Washington Heights South': 4.7, 'North Corona': 5.66, "Mariner's Harbor-Arlington-Port Ivory-Granite": 3.66, 'Ocean Parkway South': 4.38, 'Allerton-Pelham Gardens': 4.19, 'Baisley Park': 4.23, 'Homecrest': 5.1, 'New Brighton-Silver Lake': 4.51, 'Williamsburg': 6.17, 'SoHo-TriBeCa-Civic Center-Little Italy': 6.03, "Annadale-Huguenot-Prince's Bay-Eltingville": 4.19, 'Far Rockaway-Bayswater': 3.87, 'Hollis': 3.4, 'Sunset Park West': 5.41, 'Pelham Bay-Country Club-City Island': 3.56, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 2.4, 'Midtown-Midtown South': 6.17, 'Soundview-Bruckner': 4.8, 'Highbridge': 4.95, 'Eastchester-Edenwald-Baychester': 3.58, 'Norwood': 4.91, 'Queensboro Hill': 4.82, 'Spuyten Duyvil-Kingsbridge': 4.62, 'East Village': 5.71, 'Bensonhurst East': 4.65, 'Springfield Gardens North': 3.5, 'West Brighton': 3.97, 'Starrett City': 2.56, 'Flatbush': 5.03, 'Lincoln Square': 5.03, 'Turtle Bay-East Midtown': 5.8, 'Cambria Heights': 2.89, 'East Concourse-Concourse Village': 4.61, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 4.82, 'Carroll Gardens-Columbia Street-Red Hook': 5.18, 'Central Harlem South': 4.16, 'Marble Hill-Inwood': 4.64, 'College Point': 3.95, 'Flushing': 5.44, 'Woodside': 5.36, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 5.19, 'Crown Heights South': 4.56, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 4.17, 'Douglas Manor-Douglaston-Little Neck': 3.47, 'Prospect Lefferts Gardens-Wingate': 4.56, 'Claremont-Bathgate': 4.88, 'Fordham South': 5.12, 'Pomonok-Flushing Heights-Hillcrest': 6.01, 'Upper East Side-Carnegie Hill': 6.43, 'Soundview-Castle Hill-Clason Point-Harding Pa': 4.8, 'Jackson Heights': 5.53, 'Kingsbridge Heights': 4.62, 'Whitestone': 4.09, 'Charleston-Richmond Valley-Tottenville': 3.37, 'Briarwood-Jamaica Hills': 4.78, 'Clinton': 7.03, 'Sunset Park East': 5.41, 'East Harlem North': 3.09, 'Stuyvesant Heights': 4.53, 'Van Cortlandt Village': 4.61, 'Schuylerville-Throgs Neck-Edgewater Park': 4.26, 'Washington Heights North': 5.69, 'East Elmhurst': 3.81, 'East Harlem South': 5.04, 'Rego Park': 4.39, 'St. Albans': 3.76, 'Mott Haven-Port Morris': 4.5, 'Lower East Side': 5.9, 'Lindenwood-Howard Beach': 3.69, 'Auburndale': 4.86, 'Stapleton-Rosebank': 4.52, 'Fort Greene': 4.88, 'Van Nest-Morris Park-Westchester Square': 4.78, 'Kensington-Ocean Parkway': 4.83, 'Elmhurst': 5.05, 'Ft. Totten-Bay Terrace-Clearview': 2.77, 'Canarsie': 4.47}
# nb_count() from 4/28/16
nb_liquor_count = {'Canarsie': 87, 'Washington Heights North': 296, 'Bayside-Bayside Hills': 102, 'Grymes Hill-Clifton-Fox Hills': 91, 'Van Cortlandt Village': 100, 'Auburndale': 129, 'East Flushing': 230, 'East Williamsburg': 479, 'Steinway': 127, 'Lenox Hill-Roosevelt Island': 80, 'Claremont-Bathgate': 132, 'South Ozone Park': 23, 'Bushwick South': 210, 'Gravesend': 164, 'Williamsburg': 479, 'Midtown-Midtown South': 480, 'Gramercy': 541, 'Jamaica': 97, 'Great Kills': 52, 'Bronxdale': 119, 'Woodside': 213, 'Flatlands': 124, 'Clinton Hill': 131, 'Bensonhurst West': 151, 'South Jamaica': 41, 'East Tremont': 132, 'Grasmere-Arrochar-Ft. Wadsworth': 65, 'Battery Park City-Lower Manhattan': 252, 'Allerton-Pelham Gardens': 66, 'East Village': 303, 'University Heights-Morris Heights': 126, 'Central Harlem North-Polo Grounds': 24, 'East Harlem North': 22, 'Eastchester-Edenwald-Baychester': 36, 'Lincoln Square': 153, 'Jackson Heights': 252, 'Co-Op City': 36, 'Elmhurst': 156, 'Bay Ridge': 210, 'Queens Village': 29, 'West New Brighton-New Brighton-St. George': 53, 'Crown Heights North': 96, 'West Farms-Bronx River': 88, 'Parkchester': 119, 'East New York': 183, 'Hunts Point': 35, 'Brownsville': 119, 'Westerleigh': 126, 'St. Albans': 43, 'Bellerose': 22, 'Prospect Heights': 224, 'Crotona Park East': 88, 'Douglas Manor-Douglaston-Little Neck': 32, 'Clinton': 1134, 'Erasmus': 153, 'Old Town-Dongan Hills-South Beach': 92, 'Springfield Gardens North': 33, 'Kensington-Ocean Parkway': 125, 'Mount Hope': 541, 'Morningside Heights': 117, 'Mott Haven-Port Morris': 90, 'New Springville-Bloomfield-Travis': 126, 'North Corona': 288, 'Schuylerville-Throgs Neck-Edgewater Park': 71, 'New Dorp-Midland Beach': 82, 'Briarwood-Jamaica Hills': 119, 'Charleston-Richmond Valley-Tottenville': 29, 'Old Astoria': 84, 'College Point': 52, 'Sunset Park West': 223, 'Madison': 114, 'Oakland Gardens': 35, 'Kingsbridge Heights': 102, 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 65, 'Elmhurst-Maspeth': 156, 'Belmont': 168, 'Upper West Side': 379, 'Queensbridge-Ravenswood-Long Island City': 394, 'Middle Village': 48, 'Hammels-Arverne-Edgemere': 8, 'Corona': 288, 'Melrose South-Mott Haven North': 100, 'Queensboro Hill': 124, 'Fresh Meadows-Utopia': 34, 'Stapleton-Rosebank': 92, 'Midwood': 80, 'Woodlawn-Wakefield': 67, 'Van Nest-Morris Park-Westchester Square': 119, "Mariner's Harbor-Arlington-Port Ivory-Granite": 39, 'Fordham South': 168, 'North Riverdale-Fieldston-Riverdale': 32, 'Stuyvesant Town-Cooper Village': 497, 'Marble Hill-Inwood': 104, 'Central Harlem South': 64, 'Windsor Terrace': 309, 'Morrisania-Melrose': 119, 'Ocean Hill': 93, 'Bedford': 127, 'Dyker Heights': 67, 'Seagate-Coney Island': 81, 'Ridgewood': 279, 'Bath Beach': 151, 'Rosedale': 27, 'Whitestone': 60, 'Bushwick North': 210, 'Hamilton Heights': 100, 'Flushing': 230, 'Jamaica Estates-Holliswood': 30, 'East Harlem South': 155, 'Cypress Hills-City Line': 167, 'Lindenwood-Howard Beach': 40, 'Murray Hill': 350, 'Far Rockaway-Bayswater': 48, 'West Concourse': 100, 'Prospect Lefferts Gardens-Wingate': 96, 'Crown Heights South': 96, 'Murray Hill-Kips Bay': 350, 'Borough Park': 100, 'Washington Heights South': 110, 'Lower East Side': 364, 'Upper East Side-Carnegie Hill': 618, 'Richmond Hill': 92, 'Hunters Point-Sunnyside-West Maspeth': 93, 'SoHo-TriBeCa-Civic Center-Little Italy': 417, 'Stuyvesant Heights': 93, 'Carroll Gardens-Columbia Street-Red Hook': 178, 'Astoria': 176, 'Homecrest': 164, 'Maspeth': 84, 'West Village': 711, 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 451, 'Hollis': 30, 'Soundview-Castle Hill-Clason Point-Harding Pa': 121, 'Pelham Bay-Country Club-City Island': 35, 'New Brighton-Silver Lake': 91, 'Glendale': 279, 'Bensonhurst East': 105, 'Springfield Gardens South-Brookville': 33, 'Williamsbridge-Olinville': 194, 'Highbridge': 141, 'Turtle Bay-East Midtown': 329, 'Yorkville': 157, 'Woodhaven': 70, 'East Concourse-Concourse Village': 100, 'Flatbush': 153, 'Kew Gardens': 31, 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 11, 'Bedford Park-Fordham North': 168, 'Fort Greene': 131, 'West Brighton': 53, 'Rossville-Woodrow': 62, 'Soundview-Bruckner': 121, 'East Flatbush-Farragut': 115, 'Baisley Park': 69, 'Ocean Parkway South': 80, 'Brooklyn Heights-Cobble Hill': 257, 'East New York (Pennsylvania Ave)': 183, 'Rego Park': 81, 'Sunset Park East': 223, 'Chinatown': 332, 'Cambria Heights': 18, 'Forest Hills': 151, 'Glen Oaks-Floral Park-New Hyde Park': 100, 'Westchester-Unionport': 132, 'Longwood': 90, 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 124, 'Brighton Beach': 179, 'Kew Gardens Hills': 31, 'Norwood': 136, 'Oakwood-Oakwood Beach': 82, 'Manhattanville': 117, 'Port Richmond': 63, 'Rugby-Remsen Village': 115, 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 179, 'Starrett City': 13, 'Spuyten Duyvil-Kingsbridge': 102, 'Ozone Park': 58, 'Laurelton': 33, 'Hudson Yards-Chelsea-Flat Iron-Union Square': 726, 'Greenpoint': 231, "Annadale-Huguenot-Prince's Bay-Eltingville": 66, 'Pomonok-Flushing Heights-Hillcrest': 408, 'Ft. Totten-Bay Terrace-Clearview': 16, 'East Elmhurst': 45}