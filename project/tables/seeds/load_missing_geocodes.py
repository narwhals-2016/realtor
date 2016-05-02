from tables.models import Neighborhood

missing_gecodes = {
	'Allerton-Pelham Gardens': ['10312', '40.543117','-74.17628'],
	"Annadale-Huguenot-Prince's Bay-Eltingville": ['10312','40.543117','-74.17628'],
	'Arden Heights': ['10312','40.5446','-74.1795'],
	# 'Astoria': '11103',---
	# 'Auburndale': '11358',---
	# 'Baisley Park': '11434',---
	# 'Bath Beach': '11214',---
	'Battery Park City-Lower Manhattan': ['10280', '40.707467','-74.0178'],
	# 'Bay Ridge': '11209', ---
	# 'Bayside-Bayside Hills': '11361', ----
	'Bedford Park-Fordham North': ['10458', '40.864166','-73.88881'],
	# 'Bedford brooklyn': '11216',---
	# 'Bellerose': '11426',---
	# 'Belmont bronx': '10458',---
	# 'Bensonhurst East': '11204', ---
	# 'Bensonhurst West': '11214',----
	# 'Borough Park': '11219', ----
	'Breezy Point-Belle Harbor-Rockaway Park-Broad': ['11697','40.560167', '-73.90891'],
	'Briarwood-Jamaica Hills': ['11435', '40.700068', '-73.80986'],
	# 'Brighton Beach': '11235', ---
	# 'Bronxdale': '10462', ---
	# 'Brooklyn Heights-Cobble Hill': '11201', ---
	# 'Brownsville': '11212', ---
	# 'Bushwick North': '11237', ---
	# 'Bushwick South': '11237', ---
	# 'Cambria Heights': '11411', --
	# 'Canarsie': '11236', ---
	'Carroll Gardens-Columbia Street-Red Hook': ['11231', '40.6788','-74.00254'],
	'Central Harlem North-Polo Grounds': ['10039', '40.826181', '-73.9371'],
	'Central Harlem South': ['10026', '40.802853','-73.95471'],
	'Charleston-Richmond Valley-Tottenville': ['10307', '40.495929', '-74.210085'],
	# 'Chinatown': '10013', ---
	'Claremont-Bathgate': ['10457', '40.846745','-73.89861'],
	# 'Clinton Hill': '11205', ---
	# 'Co-Op City': '10475',---
	# 'College Point': '11356', ---
	# 'Corona': '11368', ---
	# 'Crotona Park East': '10460', ---
	# 'Crown Heights North': '11225', ---
	# 'Crown Heights South': '11225', ---
	# 'Cypress Hills-City Line': '11208', ---
	'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': ['11201','40.699252', '-73.987822'],
	# 'Douglas Manor-Douglaston-Little Neck': '11362', ---
	# 'Dyker Heights': '11228', ---
	'East Concourse-Concourse Village': ['10451', '40.819729','-73.9223'],
	# 'East Elmhurst': '11369', ---
	'East Flatbush-Farragut': ['11203', '40.649059', '-73.93304'],
	# 'East Flushing': '11354', ---
	# 'East Harlem North': '10037', ---
	# 'East Harlem South': '10029', ---
	# 'East New York': '11207', ---
	'East New York (Pennsylvania Ave)': ['11207', '40.670874', '-73.89424'],
	# 'East Tremont': '10457', ---
	# 'East Village': '10009', ---
	# 'East Williamsburg': '11211', 
	'Eastchester-Edenwald-Baychester': ['10475', '40.878522','-73.82541'],
	'Elmhurst': ['11373', '40.736076','-73.87804'],
	'Elmhurst-Maspeth': ['11373', '40.736076', '-73.87804'],
	# 'Erasmus': '11226',
	'Far Rockaway-Bayswater': ['11691','40.60002', '-73.75962'],
	# 'Flatbush': '11226',
	# 'Flatlands': '11234',
	# 'Flushing': '11354',
	# 'Fordham South': '10458',
	# 'Forest Hills': '11375',
	# 'Fort Greene': '11205',
	'Fresh Meadows-Utopia': ['11365', '40.738983','-73.79209'],
	'Ft. Totten-Bay Terrace-Clearview': ['11360','40.780386', '-73.78005'],
	'Georgetown-Marine Park-Bergen Beach-Mill Basi': ['11234', '40.618561', '-73.9216'],
	'Glen Oaks-Floral Park-New Hyde Park': ['11040', '40.742901', '-73.67895'],
	# 'Glendale': '11385',
	# 'Gramercy': '10003',
	'Grasmere-Arrochar-Ft. Wadsworth': ['10304', '40.60787','-74.08991'], 
	# 'Gravesend': '11223',
	# 'Great Kills': '10308',
	# 'Greenpoint': '11222',
	'Grymes Hill-Clifton-Fox Hills': ['10301', '40.631775', '-74.09432'],
	# 'Hamilton Heights': '10031',
	'Hammels-Arverne-Edgemere': ['11692', '40.592939','-73.79568'],
	# 'Highbridge': '10452',
	# 'Hollis': '11423',
	# 'Homecrest': '11223',
	'Hudson Yards-Chelsea-Flat Iron-Union Square': ['10011', '40.741012','-74.00012'],
	'Hunters Point-Sunnyside-West Maspeth': ['11104', '40.743796','-73.91949'],
	# 'Hunts Point': '10474',
	# 'Jackson Heights': '11372',
	# 'Jamaica': '11432',
	'Jamaica Estates-Holliswood': ['11423', '40.714261','-73.76824'],
	'Kensington-Ocean Parkway': ['11218', '40.644552','-73.97595'],
	# 'Kew Gardens': '11415',
	# 'Kew Gardens Hills': '11415',
	# 'Kingsbridge Heights': '10463',
	# 'Laurelton': '11413',
	'Lenox Hill-Roosevelt Island': ['10065','40.7656','-73.9624'],
	# 'Lincoln Square': '10023',
	'Lindenwood-Howard Beach': ['11414','40.65054','-73.839715'],
	# 'Longwood': '10455',
	# 'Lower East Side': '10002',
	# 'Madison brookl': '11229',
	# 'Manhattanville': '10027',
	'Marble Hill-Inwood': ['10034', '40.867653','-73.92'],
	"Mariner's Harbor-Arlington-Port Ivory-Granite": ['10303', '40.629448','-74.16239'],
	# 'Maspeth': '11378',
	'Melrose South-Mott Haven North': ['10451', '40.819729','-73.9223'],
	# 'Middle Village': '11379',
	# 'Midtown-Midtown South': '10019',
	# 'Midwood': '11230',
	# 'Morningside Heights': '10027',
	# 'Morrisania-Melrose': '10456',
	# 'Mott Haven-Port Morris': '10454',
	# 'Mount Hope': '10003',
	# 'Murray Hill': '10016',
	'Murray Hill-Kips Bay': ['10016', '40.74618','-73.97759'],
	'New Brighton-Silver Lake': ['10301','40.631775','-74.09432'],
	# 'New Dorp-Midland Beach': '10306',
	# 'New Springville-Bloomfield-Travis': '10314',
	# 'North Corona': '11368',
	# 'North Riverdale-Fieldston-Riverdale': '10471',
	'North Side-South Side': ['11211','40.7111','-73.9565'],
	# 'Norwood': '10467',
	# 'Oakland Gardens': '11364',
	# 'Oakwood-Oakwood Beach': '10306',
	# 'Ocean Hill': '11233',
	# 'Ocean Parkway South': '11230',
	# 'Old Astoria': '11102',
	'Old Town-Dongan Hills-South Beach': ['10305','40.599021','-74.07503'],
	# 'Ozone Park': '11417',
	# 'Parkchester': '10462',
	'Pelham Bay-Country Club-City Island': ['10464', '40.857017','-73.78903'],
	# 'Pelham Parkway': '10062',
	'Pomonok-Flushing Heights-Hillcrest': ['11354','40.767969','-73.82496'],
	# 'Port Richmond': '10302',
	# 'Prospect Heights': '11238',
	'Prospect Lefferts Gardens-Wingate': ['11225','40.662892', '-73.95509'],
	'Park Slope-Gowanus': ['11215', '40.66658', '-73.977418']
	# 'Queens Village': '11428',
	# 'Queensboro Hill queens': '11355',
	'Queensbridge-Ravenswood-Long Island City': ['11106', '40.762012','-73.93147'], 
	# 'Rego Park': '11374',
	# 'Richmond Hill': '11418',
	# 'Ridgewood': '11385',
	# 'Rikers Island': 'MISSING',
	# 'Rosedale': '11422',
	'Rossville-Woodrow': ['10309', '40.529749', '-74.21304'],
	# 'Clinton' : ["10036",'10019',"10018"],
	'Rugby-Remsen Village': ['11203', '40.649059','-73.93304'],
	'Schuylerville-Throgs Neck-Edgewater Park': ['10465', '40.825727','-73.81752'],
	'Seagate-Coney Island': ['11224','40.576589', '-73.99172'],
	'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': ['11235', '40.583803', '-73.95019'],
	'SoHo-TriBeCa-Civic Center-Little Italy': ['10013','40.720666','-74.00526'],
	'Soundview-Bruckner': ['10472', '40.830409','-73.86845'],
	'Soundview-Castle Hill-Clason Point-Harding Pa': ['10472', '40.830409', '-73.86845'],
	# 'South Jamaica': '11433',
	# 'South Ozone Park': '11436',
	# 'Springfield Gardens North': '11413',
	'Springfield Gardens South-Brookville': ['11413','40.670138', '-73.75141'],
	'Spuyten Duyvil-Kingsbridge': ['10463', '40.881086','-73.90749'],
	# 'St. Albans': '11412',
	'Stapleton-Rosebank': ['10305', '40.599021','-74.07503'],
	# 'Starrett City': '11239',
	# 'Steinway': '11105',
	# 'Stuyvesant Heights nyc': '11233',
	'Stuyvesant Town-Cooper Village': ['10009','40.727093','-73.97864'],
	# 'Sunset Park East': '11220',
	# 'Sunset Park West': '11220',
	'Todt Hill-Emerson Hill-Heartland Village-Ligh': ['10304', '40.60787', '-74.08991'],
	'Turtle Bay-East Midtown': ['10022', '40.759015','-73.96732'],
	# 'University Heights-Morris Heights': '10453',
	'Upper East Side-Carnegie Hill': ['10128','40.781894','-73.95039'],
	# 'Upper West Side': ['10024',"10025"],
	'Van Cortlandt Village': ['10468', '40.867107','-73.89916'],
	'Van Nest-Morris Park-Westchester Square': ['10462', '40.842173','-73.85862'],
	# 'Washington Heights North': ['10040',"10032",'10033'],
	# 'Washington Heights South': '10033',
	# 'West Brighton': '10310',
	# 'West Concourse': '10451',
	'West Farms-Bronx River': ['10460', '40.84095','-73.88036'],
	'West New Brighton-New Brighton-St. George': ['10310', '40.63212', '-74.11551'],
	# 'West Village': ['10014',"10012"],
	# 'Westchester-Unionport': '10461',
	# 'Westerleigh': '10314',
	# 'Whitestone': '11357',
	'Williamsbridge-Olinville': ['10467', '40.872265','-73.86937'],
	# 'Williamsburg': '11211',
	# 'Windsor Terrace': '11215',
	# 'Woodhaven': '11421',
	'Woodlawn-Wakefield': ['10466', '40.89095','-73.84702'],
	# 'Woodside': '11377',
	# 'Yorkville nyc': '10128',
	# "hell's kitchen": '10019',
}

def load_geos(nb_dict):
	# geocodes are taken from zipcode-geocodes file from internet and harcoded them 
	# in the above missing_geocodes dictionary which is a subset of best_matches dictionary,
	# as the realtor project is based on neighborhood as the primary key for all information
	for k, val in nb_dict.items():
		temp = Neighborhood.objects.get(name=k)
		temp.latitude  = val[1]
		temp.longitude = val[2] 
		temp.save()

def run():
	load_geos(missing_gecodes)