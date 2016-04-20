"""
arrays pulled from infoshare.org -> Area Comparison page, via infoshare.js script
"""
bronx_array = [
"10451 - Melrose", 
"10452 - Highbridge", 
"10453 - Morris Heights", 
"10454 - Mott Haven/Port Morris",
"10455 - The Hub/Longwood", 
"10456 - Morrisania", 
"10457 - Tremont/East Tremont", 
"10458 - Belmont/Fordham/Bedford Park", 
"10459 - Longwood/Morrisania", 
"10460 - West Farms/Crotona", 
"10461 - Westchester/Morris Park", 
"10462 - Parkchester/Van Nest", 
"10463 - Kingsbridge (Bronx only)", 
"10464 - City Island", 
"10465 - Throgs Neck/Country Club", 
"10466 - Wakefield", 
"10467 - Norwood/Williamsbridge", 
"10468 - University Heights", 
"10469 - Williamsbridge/Baychester", 
"10470 - Woodlawn/Wakefield", 
"10471 - Riverdale/Fieldston", 
"10472 - Soundview", 
"10473 - Clasons Point", 
"10474 - Hunts Point", 
"10475 - Co-op City/Eastchester", 
"11370 - Jackson Heights-Rikers Island (Bronx only)"
]
brooklyn_array = ["11201 - Brooklyn Heights/Cobble Hill", "11203 - East Flatbush", "11204 - Parkville/Bensonhurst", "11205 - Fort Greene", "11206 - Williamsburg/Bedford-Stuyvesant", "11207 - East New York", "11208 - Cypress Hills", "11209 - Bay Ridge", "11210 - Vanderveer", "11211 - Williamsburg", "11212 - Brownsville", "11213 - Brower Park/Crown Heights", "11214 - Bath Beach/Bensonhurst", "11215 - Park Slope/Windsor Terrace", "11216 - Bedford-Stuyvesant", "11217 - Park Slope/Gowanus", "11218 - Kensington/Windsor Terrace", "11219 - Borough Park", "11220 - Sunset Park", "11221 - Bushwick/Bedford-Stuyvesant", "11222 - Greenpoint", "11223 - Gravesend/Homecrest", "11224 - Coney Island", "11225 - Crown Heights", "11226 - Flatbush", "11228 - Dyker Heights", "11229 - Homecrest/Madison", "11230 - Midwood", "11231 - Carroll Gardens/Red Hook", "11232 - Industry City/Sunset Park", "11233 - Stuyvesant Heights", "11234 - Flatlands/Mill Basin", "11235 - Sheepshead Bay/Brighton Beach", "11236 - Canarsie", "11237 - Bushwick", "11238 - Prospect Heights", "11239 - Starrett City"]
manhattan_array = ["10001 - Fur-Flower District", "10002 - Chinatown/Lower East Side", "10003 - Cooper Square/Union Square", "10004 - Battery/Governors Island", "10005 - Wall Street", "10006 - Trinity", "10007 - City Hall", "10009 - East Village/Stuyvesant Town", "10010 - Madison Square/Cooper Village", "10011 - Chelsea", "10012 - Village/Noho/Soho", "10013 - Tribeca/Chinatown", "10014 - Greenwich Village", "10016 - Murray Hill", "10017 - Grand Central/United Nations", "10018 - Garment District", "10019 - Midtown/Clinton", "10020 - Rockefeller Center", "10021 - Lenox Hill", "10022 - Sutton Place/Beekman Place", "10023 - Lincoln Center/Ansonia", "10024 - Upper West Side", "10025 - Cathedral", "10026 - Central Harlem, South", "10027 - Manhattanville", "10028 - Yorkville", "10029 - East Harlem, South", "10030 - Central Harlem, Middle", "10031 - Hamilton Heights", "10032 - South Washington Heights", "10033 - Washington Heights", "10034 - Inwood", "10035 - East Harlem, Middle", "10036 - Theatre District/Clinton", "10037 - East Harlem, North", "10038 - South St. Seaport/Chinatown", "10039 - Central Harlem, North", "10040 - North Washington Heights", "10044 - Roosevelt Island", "10128 - Yorkville", "10280 - Battery Park City", "10463 - Kingsbridge (Manhattan only)"]
queens_array = ["11001 - Floral Park", "11004 - Glen Oaks", "11005 - North Shore Towers", "11040 - New Hyde Park", "11101 - Long Island City/Hunters Point", "11102 - Old Astoria", "11103 - Astoria", "11104 - Sunnyside", "11105 - Steinway", "11106 - Ravenswood", "11354 - Flushing", "11355 - Flushing/Murray Hill", "11356 - College Point", "11357 - Whitestone", "11358 - Auburndale", "11360 - Bay Terrace", "11361 - Bayside", "11362 - Little Neck", "11363 - Douglaston", "11364 - Oakland Gardens/Bayside Hill", "11365 - Fresh Meadows", "11366 - Utopia/Fresh Meadows", "11367 - Kew Garden Hills", "11368 - Corona", "11369 - East Elmhurst", "11370 - Jackson Heights-Rikers Island(Queens only)", "11372 - Jackson Heights", "11373 - Elmhurst", "11374 - Rego Park", "11375 - Forest Hills", "11377 - Woodside", "11378 - Maspeth", "11379 - Middle Village", "11385 - Ridgewood/Glendale", "11411 - Cambria Heights", "11412 - St. Albans", "11413 - Springfield Gardens/Laurelton", "11414 - Howard Beach", "11415 - Kew Gardens", "11416 - Ozone Park/Woodhaven", "11417 - Ozone Park", "11418 - Richmond Hill", "11419 - South Richmond Hill", "11420 - South Ozone Park", "11421 - Woodhaven", "11422 - Rosedale", "11423 - Hollis/Holliswood", "11426 - Bellerose", "11427 - Queens Village/Creedmoor", "11428 - Queens Village", "11429 - Queens Village (South)", "11430 - JFK Airport", "11432 - Jamaica/Hillcrest", "11433 - South Jamaica", "11434 - Rochdale/Baisley Park", "11435 - Jamaica Hills/South Jamaica", "11436 - South Ozone Park", "11691 - Far Rockaway", "11692 - Arverne", "11693 - Hammels/Broad Channel", "11694 - Seaside/Belle Harbour/Neponsit", "11695 - Fort Tilden", "11697 - Rockaway Point/Roxbury"]
staten_island_array = ["10301 - New Brighton/Grymes Hill", "10302 - Port Richmond", "10303 - Mariners Harbour/Point Ivory", "10304 - Stapleton/Fox Hills", "10305 - Rosebank", "10306 - New Dorp/Richmondtown", "10307 - Tottenville", "10308 - Great Kills", "10309 - Princes Bay/Woodrow", "10310 - West New Brighton", "10312 - Eltingville/Annadale", "10314 - Castleton Corners/New Springvill"]

"""
neighborhoods from jack's google-distance-api file, assuming it's list of our census nbs
"""
neighborhoods = ["Gravesend","Stapleton-Rosebank","Grasmere-Arrochar-Ft. Wadsworth","Grymes Hill-Clifton-Fox Hills","Old Town-Dongan Hills-South Beach","New Brighton-Silver Lake","New Dorp-Midland Beach","West New Brighton-New Brighton-St. George","Oakwood-Oakwood Beach","Westerleigh","Port Richmond","Borough Park","Great Kills","Todt Hill-Emerson Hill-Heartland Village-Ligh","Mariner's Harbor-Arlington-Port Ivory-Granite","Arden Heights","New Springville-Bloomfield-Travis","Rossville-Woodrow","Annadale-Huguenot-Prince's Bay-Eltingville","Charleston-Richmond Valley-Tottenville","Rosedale","Far Rockaway-Bayswater","Bensonhurst West","Springfield Gardens North","Springfield Gardens South-Brookville","Hammels-Arverne-Edgemere","Lindenwood-Howard Beach","Starrett City","East New York (Pennsylvania Ave)","East New York","Canarsie","Brownsville","Rugby-Remsen Village","Seagate-Coney Island","Breezy Point-Belle Harbor-Rockaway Park-Broad","Georgetown-Marine Park-Bergen Beach-Mill Basi","Flatlands","East Flatbush-Farragut","Madison brookl","Erasmus","Sheepshead Bay-Gerritsen Beach-Manhattan Beac","Crown Heights South","Prospect Lefferts Gardens-Wingate","Brighton Beach","Sunset Park East","Midwood","Homecrest","Flatbush","Ocean Parkway South","West Brighton","Kensington-Ocean Parkway","Windsor Terrace","Glen Oaks-Floral Park-New Hyde Park","Bellerose","Cambria Heights","Bath Beach","Douglas Manor-Douglaston-Little Neck","Queens Village","Laurelton","Oakland Gardens","Hollis","St. Albans","Jamaica Estates-Holliswood","Bayside-Bayside Hills","Fresh Meadows-Utopia","Auburndale","Dyker Heights","Ft. Totten-Bay Terrace-Clearview","Baisley Park","South Jamaica","Pomonok-Flushing Heights-Hillcrest","Jamaica","East Flushing","Briarwood-Jamaica Hills","Murray Hill","Kew Gardens Hills","Queensboro Hill queens","Sunset Park West","Flushing","South Ozone Park","Whitestone","Kew Gardens","Richmond Hill","Stuyvesant Town-Cooper Village","East Village","Greenpoint","Maspeth","Rego Park","Bay Ridge","SoHo-TriBeCa-Civic Center-Little Italy","Chinatown","Bensonhurst East","Forest Hills","Bushwick North","Fort Greene","Bedford brooklyn","Woodhaven","DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H","Bushwick South","Clinton Hill","Stuyvesant Heights nyc","Cypress Hills-City Line","Prospect Heights","Lower East Side","Ocean Hill","Ozone Park","Carroll Gardens-Columbia Street-Red Hook","Crown Heights North","Morningside Heights","Central Harlem South","Mott Haven-Port Morris","East Harlem North","Rikers Island","East Harlem South","North Side-South Side","Upper West Side","Yorkville nyc","Lincoln Square","Steinway","College Point","Old Astoria","Upper East Side-Carnegie Hill","East Elmhurst","hell's kitchen","Astoria","East Williamsburg","Lenox Hill-Roosevelt Island","Queensbridge-Ravenswood-Long Island City","Jackson Heights","North Corona","Midtown-Midtown South","Turtle Bay-East Midtown","Woodside","Hudson Yards-Chelsea-Flat Iron-Union Square","Corona","Murray Hill-Kips Bay","Williamsburg","Elmhurst-Maspeth","Gramercy","Elmhurst","West Village","Hunters Point-Sunnyside-West Maspeth","Pelham Bay-Country Club-City Island","Schuylerville-Throgs Neck-Edgewater Park","Co-Op City","Eastchester-Edenwald-Baychester","Westchester-Unionport","Battery Park City-Lower Manhattan","Allerton-Pelham Gardens","Parkchester","Pelham Parkway","Williamsbridge-Olinville","Bronxdale","Van Nest-Morris Park-Westchester Square","Woodlawn-Wakefield","West Farms-Bronx River","Soundview-Castle Hill-Clason Point-Harding Pa","Soundview-Bruckner","Glendale","Norwood","Belmont bronx","East Tremont","Crotona Park East","Bedford Park-Fordham North","Hunts Point","Longwood","Fordham South","Van Cortlandt Village","Claremont-Bathgate","Ridgewood","Kingsbridge Heights","Morrisania-Melrose","Mount Hope","North Riverdale-Fieldston-Riverdale","Spuyten Duyvil-Kingsbridge","Melrose South-Mott Haven North","East Concourse-Concourse Village","University Heights-Morris Heights","Marble Hill-Inwood","West Concourse","Brooklyn Heights-Cobble Hill","Highbridge","Washington Heights North","Washington Heights South","Central Harlem North-Polo Grounds","Hamilton Heights","Manhattanville","Middle Village"]


def make_dict(arr):
	my_dict = {}
	zip_code = 0
	nb = ""
	for el in arr:
		zip_code = el[0:5]
		nb = el[8:]
		my_dict[nb]=zip_code
	return my_dict

bronx_dict = {'Co-op City/Eastchester': '10475', 'Throgs Neck/Country Club': '10465', 'Morris Heights': '10453', 'The Hub/Longwood': '10455', 'Belmont/Fordham/Bedford Park': '10458', 'Highbridge': '10452', 'Williamsbridge/Baychester': '10469', 'Morrisania': '10456', 'Soundview': '10472', 'Norwood/Williamsbridge': '10467', 'Jackson Heights-Rikers Island (Bronx only)': '11370', 'University Heights': '10468', 'Clasons Point': '10473', 'City Island': '10464', 'Longwood/Morrisania': '10459', 'Parkchester/Van Nest': '10462', 'Kingsbridge (Bronx only)': '10463', 'Hunts Point': '10474', 'West Farms/Crotona': '10460', 'Wakefield': '10466', 'Tremont/East Tremont': '10457', 'Melrose': '10451', 'Mott Haven/Port Morris': '10454', 'Woodlawn/Wakefield': '10470', 'Westchester/Morris Park': '10461', 'Riverdale/Fieldston': '10471'}
brooklyn_dict = {'Cypress Hills': '11208', 'Bedford-Stuyvesant': '11216', 'Brownsville': '11212', 'Brower Park/Crown Heights': '11213', 'Bushwick/Bedford-Stuyvesant': '11221', 'Midwood': '11230', 'Canarsie': '11236', 'Prospect Heights': '11238', 'Starrett City': '11239', 'Industry City/Sunset Park': '11232', 'Brooklyn Heights/Cobble Hill': '11201', 'Borough Park': '11219', 'Sheepshead Bay/Brighton Beach': '11235', 'Dyker Heights': '11228', 'Williamsburg/Bedford-Stuyvesant': '11206', 'Flatbush': '11226', 'Carroll Gardens/Red Hook': '11231', 'Greenpoint': '11222', 'Flatlands/Mill Basin': '11234', 'Stuyvesant Heights': '11233', 'Parkville/Bensonhurst': '11204', 'East Flatbush': '11203', 'Vanderveer': '11210', 'Coney Island': '11224', 'Park Slope/Gowanus': '11217', 'Gravesend/Homecrest': '11223', 'Bay Ridge': '11209', 'Williamsburg': '11211', 'Sunset Park': '11220', 'Kensington/Windsor Terrace': '11218', 'Park Slope/Windsor Terrace': '11215', 'Bath Beach/Bensonhurst': '11214', 'Crown Heights': '11225', 'East New York': '11207', 'Homecrest/Madison': '11229', 'Bushwick': '11237', 'Fort Greene': '11205'}
manhattan_dict = {'East Harlem, Middle': '10035', 'Village/Noho/Soho': '10012', 'South St. Seaport/Chinatown': '10038', 'Midtown/Clinton': '10019', 'Trinity': '10006', 'Cathedral': '10025', 'East Harlem, North': '10037', 'Hamilton Heights': '10031', 'Sutton Place/Beekman Place': '10022', 'Roosevelt Island': '10044', 'Tribeca/Chinatown': '10013', 'Lenox Hill': '10021', 'Kingsbridge (Manhattan only)': '10463', 'Grand Central/United Nations': '10017', 'Garment District': '10018', 'Chelsea': '10011', 'Chinatown/Lower East Side': '10002', 'Yorkville': '10128', 'South Washington Heights': '10032', 'Rockefeller Center': '10020', 'Murray Hill': '10016', 'Battery/Governors Island': '10004', 'Fur-Flower District': '10001', 'Upper West Side': '10024', 'Cooper Square/Union Square': '10003', 'Greenwich Village': '10014', 'Central Harlem, South': '10026', 'East Harlem, South': '10029', 'Central Harlem, Middle': '10030', 'East Village/Stuyvesant Town': '10009', 'City Hall': '10007', 'Wall Street': '10005', 'North Washington Heights': '10040', 'Battery Park City': '10280', 'Lincoln Center/Ansonia': '10023', 'Theatre District/Clinton': '10036', 'Manhattanville': '10027', 'Washington Heights': '10033', 'Inwood': '10034', 'Madison Square/Cooper Village': '10010', 'Central Harlem, North': '10039'}
queens_dict = {'College Point': '11356', 'Rosedale': '11422', 'Middle Village': '11379', 'South Ozone Park': '11436', 'Rochdale/Baisley Park': '11434', 'Jackson Heights-Rikers Island(Queens only)': '11370', 'Rockaway Point/Roxbury': '11697', 'New Hyde Park': '11040', 'Rego Park': '11374', 'Auburndale': '11358', 'Oakland Gardens/Bayside Hill': '11364', 'Steinway': '11105', 'Whitestone': '11357', 'Kew Gardens': '11415', 'Corona': '11368', 'Ozone Park': '11417', 'Forest Hills': '11375', 'Astoria': '11103', 'Fort Tilden': '11695', 'Glen Oaks': '11004', 'Flushing/Murray Hill': '11355', 'East Elmhurst': '11369', 'Cambria Heights': '11411', 'Elmhurst': '11373', 'Arverne': '11692', 'Little Neck': '11362', 'Queens Village/Creedmoor': '11427', 'Queens Village (South)': '11429', 'Maspeth': '11378', 'North Shore Towers': '11005', 'Ravenswood': '11106', 'Bellerose': '11426', 'Floral Park': '11001', 'Bay Terrace': '11360', 'Hammels/Broad Channel': '11693', 'Kew Garden Hills': '11367', 'Queens Village': '11428', 'Utopia/Fresh Meadows': '11366', 'Douglaston': '11363', 'Fresh Meadows': '11365', 'Hollis/Holliswood': '11423', 'Jackson Heights': '11372', 'Sunnyside': '11104', 'Woodhaven': '11421', 'St. Albans': '11412', 'Bayside': '11361', 'Ozone Park/Woodhaven': '11416', 'Long Island City/Hunters Point': '11101', 'Jamaica Hills/South Jamaica': '11435', 'Old Astoria': '11102', 'South Jamaica': '11433', 'Springfield Gardens/Laurelton': '11413', 'Howard Beach': '11414', 'Far Rockaway': '11691', 'Woodside': '11377', 'Richmond Hill': '11418', 'Jamaica/Hillcrest': '11432', 'Seaside/Belle Harbour/Neponsit': '11694', 'JFK Airport': '11430', 'Ridgewood/Glendale': '11385', 'Flushing': '11354', 'South Richmond Hill': '11419'}
staten_island_dict = {'Port Richmond': '10302', 'Castleton Corners/New Springvill': '10314', 'Great Kills': '10308', 'Stapleton/Fox Hills': '10304', 'Princes Bay/Woodrow': '10309', 'New Brighton/Grymes Hill': '10301', 'Tottenville': '10307', 'Mariners Harbour/Point Ivory': '10303', 'Rosebank': '10305', 'New Dorp/Richmondtown': '10306', 'Eltingville/Annadale': '10312', 'West New Brighton': '10310'}
# city_dict = {
# 	**bronx_dict,
# 	**brooklyn_dict,
# 	**manhattan_dict,
# 	**queens_dict,
# 	**staten_island_dict,
# }

city_dict = {
	'Arverne': '11692',
	'Astoria': '11103',
	'Auburndale': '11358',
	'Bath Beach/Bensonhurst': '11214',
	'Battery Park City': '10280',
	'Battery/Governors Island': '10004',
	'Bay Ridge': '11209',
	'Bay Terrace': '11360',
	'Bayside': '11361',
	'Bedford-Stuyvesant': '11216',
	'Bellerose': '11426',
	'Belmont/Fordham/Bedford Park': '10458',
	'Borough Park': '11219',
	'Brooklyn Heights/Cobble Hill': '11201',
	'Brower Park/Crown Heights': '11213',
	'Brownsville': '11212',
	'Bushwick': '11237',
	'Bushwick/Bedford-Stuyvesant': '11221',
	'Cambria Heights': '11411',
	'Canarsie': '11236',
	'Carroll Gardens/Red Hook': '11231',
	'Castleton Corners/New Springvill': '10314',
	'Cathedral': '10025',
	'Central Harlem, Middle': '10030',
	'Central Harlem, North': '10039',
	'Central Harlem, South': '10026',
	'Chelsea': '10011',
	'Chinatown/Lower East Side': '10002',
	'City Hall': '10007',
	'City Island': '10464',
	'Clasons Point': '10473',
	'Co-op City/Eastchester': '10475',
	'College Point': '11356',
	'Coney Island': '11224',
	'Cooper Square/Union Square': '10003',
	'Corona': '11368',
	'Crown Heights': '11225',
	'Cypress Hills': '11208',
	'Douglaston': '11363',
	'Dyker Heights': '11228',
	'East Elmhurst': '11369',
	'East Flatbush': '11203',
	'East Harlem, Middle': '10035',
	'East Harlem, North': '10037',
	'East Harlem, South': '10029',
	'East New York': '11207',
	'East Village/Stuyvesant Town': '10009',
	'Elmhurst': '11373',
	'Eltingville/Annadale': '10312',
	'Far Rockaway': '11691',
	'Flatbush': '11226',
	'Flatlands/Mill Basin': '11234',
	'Floral Park': '11001',
	'Flushing': '11354',
	'Flushing/Murray Hill': '11355',
	'Forest Hills': '11375',
	'Fort Greene': '11205',
	'Fort Tilden': '11695',
	'Fresh Meadows': '11365',
	'Fur-Flower District': '10001',
	'Garment District': '10018',
	'Glen Oaks': '11004',
	'Grand Central/United Nations': '10017',
	'Gravesend/Homecrest': '11223',
	'Great Kills': '10308',
	'Greenpoint': '11222',
	'Greenwich Village': '10014',
	'Hamilton Heights': '10031',
	'Hammels/Broad Channel': '11693',
	'Highbridge': '10452',
	'Hollis/Holliswood': '11423',
	'Homecrest/Madison': '11229',
	'Howard Beach': '11414',
	'Hunts Point': '10474',
	'Industry City/Sunset Park': '11232',
	'Inwood': '10034',
	'JFK Airport': '11430',
	'Jackson Heights': '11372',
	'Jackson Heights-Rikers Island (Bronx only)': '11370',
	'Jackson Heights-Rikers Island(Queens only)': '11370',
	'Jamaica Hills/South Jamaica': '11435',
	'Jamaica/Hillcrest': '11432',
	'Kensington/Windsor Terrace': '11218',
	'Kew Garden Hills': '11367',
	'Kew Gardens': '11415',
	'Kingsbridge (Bronx only)': '10463',
	'Kingsbridge (Manhattan only)': '10463',
	'Lenox Hill': '10021',
	'Lincoln Center/Ansonia': '10023',
	'Little Neck': '11362',
	'Long Island City/Hunters Point': '11101',
	'Longwood/Morrisania': '10459',
	'Madison Square/Cooper Village': '10010',
	'Manhattanville': '10027',
	'Mariners Harbour/Point Ivory': '10303',
	'Maspeth': '11378',
	'Melrose': '10451',
	'Middle Village': '11379',
	'Midtown/Clinton': '10019',
	'Midwood': '11230',
	'Morris Heights': '10453',
	'Morrisania': '10456',
	'Mott Haven/Port Morris': '10454',
	'Murray Hill': '10016',
	'New Brighton/Grymes Hill': '10301',
	'New Dorp/Richmondtown': '10306',
	'New Hyde Park': '11040',
	'North Shore Towers': '11005',
	'North Washington Heights': '10040',
	'Norwood/Williamsbridge': '10467',
	'Oakland Gardens/Bayside Hill': '11364',
	'Old Astoria': '11102',
	'Ozone Park': '11417',
	'Ozone Park/Woodhaven': '11416',
	'Park Slope/Gowanus': '11217',
	'Park Slope/Windsor Terrace': '11215',
	'Parkchester/Van Nest': '10462',
	'Parkville/Bensonhurst': '11204',
	'Port Richmond': '10302',
	'Princes Bay/Woodrow': '10309',
	'Prospect Heights': '11238',
	'Queens Village': '11428',
	'Queens Village (South)': '11429',
	'Queens Village/Creedmoor': '11427',
	'Ravenswood': '11106',
	'Rego Park': '11374',
	'Richmond Hill': '11418',
	'Ridgewood/Glendale': '11385',
	'Riverdale/Fieldston': '10471',
	'Rochdale/Baisley Park': '11434',
	'Rockaway Point/Roxbury': '11697',
	'Rockefeller Center': '10020',
	'Roosevelt Island': '10044',
	'Rosebank': '10305',
	'Rosedale': '11422',
	'Seaside/Belle Harbour/Neponsit': '11694',
	'Sheepshead Bay/Brighton Beach': '11235',
	'Soundview': '10472',
	'South Jamaica': '11433',
	'South Ozone Park': '11436',
	'South Richmond Hill': '11419',
	'South St. Seaport/Chinatown': '10038',
	'South Washington Heights': '10032',
	'Springfield Gardens/Laurelton': '11413',
	'St. Albans': '11412',
	'Stapleton/Fox Hills': '10304',
	'Starrett City': '11239',
	'Steinway': '11105',
	'Stuyvesant Heights': '11233',
	'Sunnyside': '11104',
	'Sunset Park': '11220',
	'Sutton Place/Beekman Place': '10022',
	'The Hub/Longwood': '10455',
	'Theatre District/Clinton': '10036',
	'Throgs Neck/Country Club': '10465',
	'Tottenville': '10307',
	'Tremont/East Tremont': '10457',
	'Tribeca/Chinatown': '10013',
	'Trinity': '10006',
	'University Heights': '10468',
	'Upper West Side': '10024',
	'Utopia/Fresh Meadows': '11366',
	'Vanderveer': '11210',
	'Village/Noho/Soho': '10012',
	'Wakefield': '10466',
	'Wall Street': '10005',
	'Washington Heights': '10033',
	'West Farms/Crotona': '10460',
	'West New Brighton': '10310',
	'Westchester/Morris Park': '10461',
	'Whitestone': '11357',
	'Williamsbridge/Baychester': '10469',
	'Williamsburg': '11211',
	'Williamsburg/Bedford-Stuyvesant': '11206',
	'Woodhaven': '11421',
	'Woodlawn/Wakefield': '10470',
	'Woodside': '11377',
	'Yorkville': '10128'
}

"""
48 exact matches
"""
def check_matches(nb_list, city_dict):
	match_count = 0
	missing_count = 0
	match_dict = {}
	missing_dict = {}
	for nb in nb_list:
		if city_dict.get(nb):
			match_dict[nb] = city_dict[nb]
			match_count += 1
		else:
			missing_dict[nb] = 'missing'
			missing_count += 1
	return {
		'match_count': match_count,
		'missing_count': missing_count,
		'match_dict': match_dict,
		'missing_dict': missing_dict,
	}
"""
27 additional matches--but in some cases the same neighborhood is in multiple boroughs, may cause confusion
"""
def make_fuzzy(dictionary):
	fuzzy = {}
	for key in dictionary:
		# splits zip - nb dictionary 
		if '/' in key:
			nb_list = key.split('/')			
			for nb in nb_list:
				fuzzy[nb] = dictionary[key]
			# [fuzzy[nb] = dictionary[key] for nb in nb_list]
	return fuzzy

# make_fuzzy(city_dict)
fuzzy_dict = {'Oakland Gardens': '11364', 'Tremont': '10457', 'Seaside': '11694', 'Carroll Gardens': '11231', 'Clinton': '10019', 'The Hub': '10455', 'Crown Heights': '11213', 'Brooklyn Heights': '11201', 'West Farms': '10460', 'Mott Haven': '10454', 'Hollis': '11423', 'Industry City': '11232', 'New Dorp': '10306', 'Van Nest': '10462', 'Fieldston': '10471', 'Queens Village': '11427', 'South Jamaica': '11435', 'Tribeca': '10013', 'Flushing': '11355', 'Bushwick': '11221', 'Brower Park': '11213', 'Cooper Village': '10010', 'Ozone Park': '11416', 'Sheepshead Bay': '11235', 'Rochdale': '11434', 'Battery': '10004', 'Village': '10012', 'Long Island City': '11101', 'Woodlawn': '10470', 'Midtown': '10019', 'Cobble Hill': '11201', 'Holliswood': '11423', 'Park Slope': '11215', 'Madison Square': '10010', 'Castleton Corners': '10314', 'Eltingville': '10312', 'Country Club': '10465', 'Norwood': '10467', 'Sutton Place': '10022', 'Jamaica Hills': '11435', 'Riverdale': '10471', 'Richmondtown': '10306', 'Morris Park': '10461', 'Bedford-Stuyvesant': '11221', 'Woodrow': '10309', 'New Brighton': '10301', 'Princes Bay': '10309', 'Creedmoor': '11427', 'Grymes Hill': '10301', 'Ridgewood': '11385', 'Woodhaven': '11416', 'Windsor Terrace': '11215', 'Mill Basin': '11234', 'Westchester': '10461', 'Stapleton': '10304', 'Lower East Side': '10002', 'Grand Central': '10017', 'Homecrest': '11223', 'Baisley Park': '11434', 'Gowanus': '11217', 'East Tremont': '10457', 'Point Ivory': '10303', 'Theatre District': '10036', 'Belmont': '10458', 'Belle Harbour': '11694', 'Broad Channel': '11693', 'Cooper Square': '10003', 'Union Square': '10003', 'Parkchester': '10462', 'Soho': '10012', 'Springfield Gardens': '11413', 'Sunset Park': '11232', 'Fresh Meadows': '11366', 'Brighton Beach': '11235', 'Bath Beach': '11214', 'Madison': '11229', 'Murray Hill': '11355', 'Fox Hills': '10304', 'Hammels': '11693', 'Laurelton': '11413', 'Red Hook': '11231', 'Chinatown': '10013', 'Hillcrest': '11432', 'Baychester': '10469', 'Williamsbridge': '10467', 'Jamaica': '11432', 'Roxbury': '11697', 'Kensington': '11218', 'Longwood': '10455', 'Stuyvesant Town': '10009', 'Port Morris': '10454', 'South St. Seaport': '10038', 'Ansonia': '10023', 'Noho': '10012', 'Eastchester': '10475', 'Williamsburg': '11206', 'Beekman Place': '10022', 'Crotona': '10460', 'East Village': '10009', 'Fordham': '10458', 'Hunters Point': '11101', 'Gravesend': '11223', 'Bayside Hill': '11364', 'Parkville': '11204', 'Rockaway Point': '11697', 'Annadale': '10312', 'Mariners Harbour': '10303', 'Wakefield': '10470', 'Neponsit': '11694', 'Lincoln Center': '10023', 'Bensonhurst': '11204', 'Co-op City': '10475', 'Governors Island': '10004', 'New Springvill': '10314', 'Flatlands': '11234', 'Throgs Neck': '10465', 'Utopia': '11366', 'Glendale': '11385', 'Morrisania': '10459', 'United Nations': '10017', 'Bedford Park': '10458'}

"""
goal: get our nbs with zip codes
"""
# match_dict for check_matches(neighborhoods, city_dict)
exact_matches = {'Whitestone': '11357', 'Starrett City': '11239', 'Woodside': '11377', 'Hamilton Heights': '10031', 'Prospect Heights': '11238', 'Bellerose': '11426', 'Richmond Hill': '11418', 'East New York': '11207', 'Old Astoria': '11102', 'Williamsburg': '11211', 'Rosedale': '11422', 'Murray Hill': '10016', 'Jackson Heights': '11372', 'Cambria Heights': '11411', 'Queens Village': '11428', 'South Jamaica': '11433', 'College Point': '11356', 'Upper West Side': '10024', 'Maspeth': '11378', 'East Elmhurst': '11369', 'Flatbush': '11226', 'Ozone Park': '11417', 'South Ozone Park': '11436', 'Bay Ridge': '11209', 'Canarsie': '11236', 'Middle Village': '11379', 'Greenpoint': '11222', 'Brownsville': '11212', 'Rego Park': '11374', 'Midwood': '11230', 'Kew Gardens': '11415', 'Highbridge': '10452', 'Forest Hills': '11375', 'Great Kills': '10308', 'Astoria': '11103', 'Flushing': '11354', 'Elmhurst': '11373', 'Port Richmond': '10302', 'Borough Park': '11219', 'Hunts Point': '10474', 'Auburndale': '11358', 'Manhattanville': '10027', 'Woodhaven': '11421', 'Steinway': '11105', 'Corona': '11368', 'St. Albans': '11412', 'Dyker Heights': '11228', 'Fort Greene': '11205'}
# missing_dict for check_matches(neighborhoods, city_dict)
missing_dict = {'Erasmus': 'missing', 'Lenox Hill-Roosevelt Island': 'missing', 'Bronxdale': 'missing', 'Oakland Gardens': 'missing', 'Central Harlem North-Polo Grounds': 'missing', 'Pelham Bay-Country Club-City Island': 'missing', 'Crotona Park East': 'missing', 'Chinatown': 'missing', 'Lindenwood-Howard Beach': 'missing', 'Yorkville nyc': 'missing', 'Seagate-Coney Island': 'missing', 'Grymes Hill-Clifton-Fox Hills': 'missing', 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 'missing', 'Hollis': 'missing', 'North Riverdale-Fieldston-Riverdale': 'missing', 'Allerton-Pelham Gardens': 'missing', 'Kew Gardens Hills': 'missing', 'Old Town-Dongan Hills-South Beach': 'missing', 'Pelham Parkway': 'missing', 'Soundview-Bruckner': 'missing', 'Hudson Yards-Chelsea-Flat Iron-Union Square': 'missing', 'Mount Hope': 'missing', 'Co-Op City': 'missing', 'Queensboro Hill queens': 'missing', 'Hammels-Arverne-Edgemere': 'missing', 'Carroll Gardens-Columbia Street-Red Hook': 'missing', 'Bedford Park-Fordham North': 'missing', 'East Concourse-Concourse Village': 'missing', 'Lincoln Square': 'missing', 'Midtown-Midtown South': 'missing', "Mariner's Harbor-Arlington-Port Ivory-Granite": 'missing', 'West New Brighton-New Brighton-St. George': 'missing', 'Pomonok-Flushing Heights-Hillcrest': 'missing', 'Soundview-Castle Hill-Clason Point-Harding Pa': 'missing', 'Ridgewood': 'missing', 'Kingsbridge Heights': 'missing', 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 'missing', 'Central Harlem South': 'missing', 'Williamsbridge-Olinville': 'missing', 'Westchester-Unionport': 'missing', 'Glen Oaks-Floral Park-New Hyde Park': 'missing', 'Bushwick South': 'missing', 'Schuylerville-Throgs Neck-Edgewater Park': 'missing', 'Kensington-Ocean Parkway': 'missing', 'Marble Hill-Inwood': 'missing', 'Battery Park City-Lower Manhattan': 'missing', 'Crown Heights South': 'missing', 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 'missing', 'Springfield Gardens North': 'missing', 'Grasmere-Arrochar-Ft. Wadsworth': 'missing', 'University Heights-Morris Heights': 'missing', 'Prospect Lefferts Gardens-Wingate': 'missing', 'Belmont bronx': 'missing', 'North Corona': 'missing', 'Fresh Meadows-Utopia': 'missing', 'Morrisania-Melrose': 'missing', 'Morningside Heights': 'missing', 'Springfield Gardens South-Brookville': 'missing', 'Norwood': 'missing', 'North Side-South Side': 'missing', 'West Brighton': 'missing', 'Bedford brooklyn': 'missing', 'Windsor Terrace': 'missing', 'Elmhurst-Maspeth': 'missing', 'Brooklyn Heights-Cobble Hill': 'missing', 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 'missing', 'Sunset Park East': 'missing', 'Lower East Side': 'missing', 'Homecrest': 'missing', 'Ocean Parkway South': 'missing', 'Baisley Park': 'missing', 'Douglas Manor-Douglaston-Little Neck': 'missing', 'Eastchester-Edenwald-Baychester': 'missing', 'East Tremont': 'missing', 'Mott Haven-Port Morris': 'missing', 'Spuyten Duyvil-Kingsbridge': 'missing', 'West Farms-Bronx River': 'missing', 'Westerleigh': 'missing', 'Bushwick North': 'missing', 'Parkchester': 'missing', 'East Harlem North': 'missing', 'Arden Heights': 'missing', 'Washington Heights South': 'missing', "hell's kitchen": 'missing', 'Bensonhurst West': 'missing', 'Brighton Beach': 'missing', 'Bath Beach': 'missing', 'East Harlem South': 'missing', 'Flatlands': 'missing', 'Melrose South-Mott Haven North': 'missing', 'Ocean Hill': 'missing', 'Stapleton-Rosebank': 'missing', 'Clinton Hill': 'missing', 'Far Rockaway-Bayswater': 'missing', 'Ft. Totten-Bay Terrace-Clearview': 'missing', 'Jamaica': 'missing', 'Laurelton': 'missing', 'Rikers Island': 'missing', 'West Village': 'missing', 'Gramercy': 'missing', 'Sunset Park West': 'missing', 'Queensbridge-Ravenswood-Long Island City': 'missing', 'Van Nest-Morris Park-Westchester Square': 'missing', 'Stuyvesant Town-Cooper Village': 'missing', 'East Flatbush-Farragut': 'missing', 'Madison brookl': 'missing', 'Rossville-Woodrow': 'missing', 'Turtle Bay-East Midtown': 'missing', 'East Village': 'missing', 'Bayside-Bayside Hills': 'missing', 'East Flushing': 'missing', 'Murray Hill-Kips Bay': 'missing', 'Gravesend': 'missing', 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 'missing', 'East New York (Pennsylvania Ave)': 'missing', 'SoHo-TriBeCa-Civic Center-Little Italy': 'missing', 'Briarwood-Jamaica Hills': 'missing', 'Cypress Hills-City Line': 'missing', 'Longwood': 'missing', 'Upper East Side-Carnegie Hill': 'missing', 'Washington Heights North': 'missing', 'Charleston-Richmond Valley-Tottenville': 'missing', "Annadale-Huguenot-Prince's Bay-Eltingville": 'missing', 'Oakwood-Oakwood Beach': 'missing', 'Crown Heights North': 'missing', 'East Williamsburg': 'missing', 'Jamaica Estates-Holliswood': 'missing', 'West Concourse': 'missing', 'Hunters Point-Sunnyside-West Maspeth': 'missing', 'Stuyvesant Heights nyc': 'missing', 'Van Cortlandt Village': 'missing', 'New Springville-Bloomfield-Travis': 'missing', 'Claremont-Bathgate': 'missing', 'New Brighton-Silver Lake': 'missing', 'Bensonhurst East': 'missing', 'Woodlawn-Wakefield': 'missing', 'Rugby-Remsen Village': 'missing', 'New Dorp-Midland Beach': 'missing', 'Fordham South': 'missing', 'Glendale': 'missing'}
# match_dict for check_matches(missing_dict.keys(), fuzzy_dict)
fuzzy_matches = {'Brighton Beach': '11235', 'Glendale': '11385', 'Homecrest': '11223', 'Baisley Park': '11434', 'Oakland Gardens': '11364', 'Flatlands': '11234', 'East Tremont': '10457', 'Jamaica': '11432', 'Bath Beach': '11214', 'Chinatown': '10013', 'Norwood': '10467', 'Ridgewood': '11385', 'Windsor Terrace': '11215', 'Longwood': '10455', 'Gravesend': '11223', 'Laurelton': '11413', 'Lower East Side': '10002', 'Hollis': '11423', 'East Village': '10009', 'Parkchester': '10462'}
# missing_dict for check_matches(missing_dict.keys(), fuzzy_dict)
fuzzy_missing = {'Erasmus': 'missing', 'Lenox Hill-Roosevelt Island': 'missing', 'Bronxdale': 'missing', 'Central Harlem North-Polo Grounds': 'missing', 'Pelham Bay-Country Club-City Island': 'missing', 'Crotona Park East': 'missing', 'Clinton Hill': 'missing', 'Lindenwood-Howard Beach': 'missing', 'Yorkville nyc': 'missing', 'Seagate-Coney Island': 'missing', 'Grymes Hill-Clifton-Fox Hills': 'missing', 'North Riverdale-Fieldston-Riverdale': 'missing', 'Allerton-Pelham Gardens': 'missing', 'Kew Gardens Hills': 'missing', 'Old Town-Dongan Hills-South Beach': 'missing', 'Pelham Parkway': 'missing', 'Soundview-Bruckner': 'missing', 'Hudson Yards-Chelsea-Flat Iron-Union Square': 'missing', 'Mount Hope': 'missing', 'Co-Op City': 'missing', 'Queensboro Hill queens': 'missing', 'Carroll Gardens-Columbia Street-Red Hook': 'missing', 'Bedford Park-Fordham North': 'missing', 'East Concourse-Concourse Village': 'missing', 'Lincoln Square': 'missing', 'Midtown-Midtown South': 'missing', "Mariner's Harbor-Arlington-Port Ivory-Granite": 'missing', 'Rossville-Woodrow': 'missing', 'West New Brighton-New Brighton-St. George': 'missing', 'Pomonok-Flushing Heights-Hillcrest': 'missing', 'Soundview-Castle Hill-Clason Point-Harding Pa': 'missing', 'Todt Hill-Emerson Hill-Heartland Village-Ligh': 'missing', 'Central Harlem South': 'missing', 'Williamsbridge-Olinville': 'missing', 'Westchester-Unionport': 'missing', 'Rikers Island': 'missing', 'Bushwick South': 'missing', 'Schuylerville-Throgs Neck-Edgewater Park': 'missing', 'Kensington-Ocean Parkway': 'missing', 'North Corona': 'missing', 'Crown Heights South': 'missing', 'Jamaica Estates-Holliswood': 'missing', 'Springfield Gardens North': 'missing', 'Grasmere-Arrochar-Ft. Wadsworth': 'missing', 'Prospect Lefferts Gardens-Wingate': 'missing', 'Belmont bronx': 'missing', 'Brooklyn Heights-Cobble Hill': 'missing', 'Westerleigh': 'missing', 'Fresh Meadows-Utopia': 'missing', 'West Village': 'missing', 'Springfield Gardens South-Brookville': 'missing', 'North Side-South Side': 'missing', 'West Brighton': 'missing', 'Bedford brooklyn': 'missing', 'Elmhurst-Maspeth': 'missing', 'Breezy Point-Belle Harbor-Rockaway Park-Broad': 'missing', 'Sunset Park East': 'missing', 'Morningside Heights': 'missing', 'Ocean Parkway South': 'missing', 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': 'missing', 'Douglas Manor-Douglaston-Little Neck': 'missing', 'Mott Haven-Port Morris': 'missing', 'Spuyten Duyvil-Kingsbridge': 'missing', 'Eastchester-Edenwald-Baychester': 'missing', 'East Williamsburg': 'missing', 'Bushwick North': 'missing', 'East Harlem North': 'missing', 'Arden Heights': 'missing', 'Van Cortlandt Village': 'missing', "hell's kitchen": 'missing', 'Bensonhurst West': 'missing', 'Sunset Park West': 'missing', 'Woodlawn-Wakefield': 'missing', 'East Harlem South': 'missing', 'Claremont-Bathgate': 'missing', 'Melrose South-Mott Haven North': 'missing', 'Stapleton-Rosebank': 'missing', 'Hammels-Arverne-Edgemere': 'missing', 'Far Rockaway-Bayswater': 'missing', 'Ft. Totten-Bay Terrace-Clearview': 'missing', 'Glen Oaks-Floral Park-New Hyde Park': 'missing', 'Morrisania-Melrose': 'missing', 'Gramercy': 'missing', 'Queensbridge-Ravenswood-Long Island City': 'missing', 'Bayside-Bayside Hills': 'missing', 'Stuyvesant Town-Cooper Village': 'missing', 'East Flatbush-Farragut': 'missing', 'Madison brookl': 'missing', 'Battery Park City-Lower Manhattan': 'missing', 'Turtle Bay-East Midtown': 'missing', 'Van Nest-Morris Park-Westchester Square': 'missing', 'East Flushing': 'missing', 'Murray Hill-Kips Bay': 'missing', 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': 'missing', 'East New York (Pennsylvania Ave)': 'missing', 'SoHo-TriBeCa-Civic Center-Little Italy': 'missing', 'Briarwood-Jamaica Hills': 'missing', 'Cypress Hills-City Line': 'missing', 'University Heights-Morris Heights': 'missing', 'Upper East Side-Carnegie Hill': 'missing', 'Washington Heights North': 'missing', 'Charleston-Richmond Valley-Tottenville': 'missing', "Annadale-Huguenot-Prince's Bay-Eltingville": 'missing', 'Oakwood-Oakwood Beach': 'missing', 'Crown Heights North': 'missing', 'Marble Hill-Inwood': 'missing', 'Georgetown-Marine Park-Bergen Beach-Mill Basi': 'missing', 'West Concourse': 'missing', 'New Dorp-Midland Beach': 'missing', 'Stuyvesant Heights nyc': 'missing', 'Ocean Hill': 'missing', 'Washington Heights South': 'missing', 'New Springville-Bloomfield-Travis': 'missing', 'New Brighton-Silver Lake': 'missing', 'Bensonhurst East': 'missing', 'West Farms-Bronx River': 'missing', 'Rugby-Remsen Village': 'missing', 'Hunters Point-Sunnyside-West Maspeth': 'missing', 'Fordham South': 'missing', 'Kingsbridge Heights': 'missing'}

# now many of remaining missing are hyphenated multiple neighborhoods. So check if 
# zip -nb is in nb_list
def zip_in_nb(nb_list, dictionary):
	matches = []
	missing = []
	for key in dictionary:
		m = [(nb, dictionary[key]) for nb in nb_list if key in nb]
		if m != []:
			matches.append(m)
	return matches

# zip_in_nb(fuzzy_missing.keys(),city_dict), 46 zip codes matched to something
zip_in_nb_results = [
	[('Fresh Meadows-Utopia', '11365')],
	[('Stuyvesant Heights nyc', '11233')],
	[('Melrose South-Mott Haven North', '10451'), ('Morrisania-Melrose', '10451')],
	[('Douglas Manor-Douglaston-Little Neck', '11363')],
	[('University Heights-Morris Heights', '10468')],
	[('Bushwick North', '11237'), ('Bushwick South', '11237')],
	[('Hunters Point-Sunnyside-West Maspeth', '11378'),
	('Elmhurst-Maspeth', '11378')],
	[('Lindenwood-Howard Beach', '11414')],
	[('Hudson Yards-Chelsea-Flat Iron-Union Square', '10011')],
	[('Glen Oaks-Floral Park-New Hyde Park', '11004')],
	[('Hunters Point-Sunnyside-West Maspeth', '11104')],
	[('Cypress Hills-City Line', '11208')],
	[('Bayside-Bayside Hills', '11361')],
	[('Woodlawn-Wakefield', '10466')],
	[('North Corona', '11368')],
	[('Murray Hill-Kips Bay', '10016')],
	[('Seagate-Coney Island', '11224')],
	[('Battery Park City-Lower Manhattan', '10280')],
	[('Pelham Bay-Country Club-City Island', '10464')],
	[('Ft. Totten-Bay Terrace-Clearview', '11360')],
	[('West New Brighton-New Brighton-St. George', '10310')],
	[('Lenox Hill-Roosevelt Island', '10021')],
	[('Far Rockaway-Bayswater', '11691')],
	[('Lenox Hill-Roosevelt Island', '10044')],
	[('Stapleton-Rosebank', '10305')],
	[('Hammels-Arverne-Edgemere', '11692')],
	[('Morrisania-Melrose', '10456')],
	[('University Heights-Morris Heights', '10453')],
	[('Glen Oaks-Floral Park-New Hyde Park', '11001')],
	[('East Flatbush-Farragut', '11226')],
	[('Sunset Park West', '11220'), ('Sunset Park East', '11220')],
	[('Glen Oaks-Floral Park-New Hyde Park', '11040')],
	[('Queensbridge-Ravenswood-Long Island City', '11106')],
	[('Elmhurst-Maspeth', '11373')],
	[('Charleston-Richmond Valley-Tottenville', '10307')],
	[('Marble Hill-Inwood', '10034')],
	[('Washington Heights South', '10033'), ('Washington Heights North', '10033')],
	[('Kew Gardens Hills', '11415')],
	[('East Williamsburg', '11211')],
	[('Crown Heights South', '11225'), ('Crown Heights North', '11225')],
	[('Yorkville nyc', '10128')],
	[('Soundview-Castle Hill-Clason Point-Harding Pa', '10472'),
	('Soundview-Bruckner', '10472')],
	[('Pomonok-Flushing Heights-Hillcrest', '11354'), ('East Flushing', '11354')],
	[('East Flatbush-Farragut', '11203')],
	[('East New York (Pennsylvania Ave)', '11207')],
	[('Douglas Manor-Douglaston-Little Neck', '11362')]
 ]

def make_pair(container):
	my_dict = {}
	for lst in container:
		for tple in lst:
			neighborhood, zip_code = tple[0], tple[1]
			my_dict[neighborhood] = zip_code
	return my_dict

# make_pair(zip_in_nb_results)
zip_dict = {
	'Battery Park City-Lower Manhattan': '10280',
	'Bayside-Bayside Hills': '11361',
	'Bushwick North': '11237',
	'Bushwick South': '11237',
	'Charleston-Richmond Valley-Tottenville': '10307',
	'Crown Heights North': '11225',
	'Crown Heights South': '11225',
	'Cypress Hills-City Line': '11208',
	'Douglas Manor-Douglaston-Little Neck': '11362',
	'East Flatbush-Farragut': '11203',
	'East Flushing': '11354',
	'East New York (Pennsylvania Ave)': '11207',
	'East Williamsburg': '11211',
	'Elmhurst-Maspeth': '11373',
	'Far Rockaway-Bayswater': '11691',
	'Fresh Meadows-Utopia': '11365',
	'Ft. Totten-Bay Terrace-Clearview': '11360',
	'Glen Oaks-Floral Park-New Hyde Park': '11040',
	'Hammels-Arverne-Edgemere': '11692',
	'Hudson Yards-Chelsea-Flat Iron-Union Square': '10011',
	'Hunters Point-Sunnyside-West Maspeth': '11104',
	'Kew Gardens Hills': '11415',
	'Lenox Hill-Roosevelt Island': '10044',
	'Lindenwood-Howard Beach': '11414',
	'Marble Hill-Inwood': '10034',
	'Melrose South-Mott Haven North': '10451',
	'Morrisania-Melrose': '10456',
	'Murray Hill-Kips Bay': '10016',
	'North Corona': '11368',
	'Pelham Bay-Country Club-City Island': '10464',
	'Pomonok-Flushing Heights-Hillcrest': '11354',
	'Queensbridge-Ravenswood-Long Island City': '11106',
	'Seagate-Coney Island': '11224',
	'Soundview-Bruckner': '10472',
	'Soundview-Castle Hill-Clason Point-Harding Pa': '10472',
	'Stapleton-Rosebank': '10305',
	'Stuyvesant Heights nyc': '11233',
	'Sunset Park East': '11220',
	'Sunset Park West': '11220',
	'University Heights-Morris Heights': '10453',
	'Washington Heights North': '10033',
	'Washington Heights South': '10033',
	'West New Brighton-New Brighton-St. George': '10310',
	'Woodlawn-Wakefield': '10466',
	'Yorkville nyc': '10128'
}

# all_matches = {**exact_matches, **fuzzy_matches, **zip_dict}
all_matches = {
	'Astoria': '11103',
	'Auburndale': '11358',
	'Baisley Park': '11434',
	'Bath Beach': '11214',
	'Battery Park City-Lower Manhattan': '10280',
	'Bay Ridge': '11209',
	'Bayside-Bayside Hills': '11361',
	'Bellerose': '11426',
	'Borough Park': '11219',
	'Brighton Beach': '11235',
	'Brownsville': '11212',
	'Bushwick North': '11237',
	'Bushwick South': '11237',
	'Cambria Heights': '11411',
	'Canarsie': '11236',
	'Charleston-Richmond Valley-Tottenville': '10307',
	'Chinatown': '10013',
	'College Point': '11356',
	'Corona': '11368',
	'Crown Heights North': '11225',
	'Crown Heights South': '11225',
	'Cypress Hills-City Line': '11208',
	'Douglas Manor-Douglaston-Little Neck': '11362',
	'Dyker Heights': '11228',
	'East Elmhurst': '11369',
	'East Flatbush-Farragut': '11203',
	'East Flushing': '11354',
	'East New York': '11207',
	'East New York (Pennsylvania Ave)': '11207',
	'East Tremont': '10457',
	'East Village': '10009',
	'East Williamsburg': '11211',
	'Elmhurst': '11373',
	'Elmhurst-Maspeth': '11373',
	'Far Rockaway-Bayswater': '11691',
	'Flatbush': '11226',
	'Flatlands': '11234',
	'Flushing': '11354',
	'Forest Hills': '11375',
	'Fort Greene': '11205',
	'Fresh Meadows-Utopia': '11365',
	'Ft. Totten-Bay Terrace-Clearview': '11360',
	'Glen Oaks-Floral Park-New Hyde Park': '11040',
	'Glendale': '11385',
	'Gravesend': '11223',
	'Great Kills': '10308',
	'Greenpoint': '11222',
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
	'Kew Gardens': '11415',
	'Kew Gardens Hills': '11415',
	'Laurelton': '11413',
	'Lenox Hill-Roosevelt Island': '10044',
	'Lindenwood-Howard Beach': '11414',
	'Longwood': '10455',
	'Lower East Side': '10002',
	'Manhattanville': '10027',
	'Marble Hill-Inwood': '10034',
	'Maspeth': '11378',
	'Melrose South-Mott Haven North': '10451',
	'Middle Village': '11379',
	'Midwood': '11230',
	'Morrisania-Melrose': '10456',
	'Murray Hill': '10016',
	'Murray Hill-Kips Bay': '10016',
	'North Corona': '11368',
	'Norwood': '10467',
	'Oakland Gardens': '11364',
	'Old Astoria': '11102',
	'Ozone Park': '11417',
	'Parkchester': '10462',
	'Pelham Bay-Country Club-City Island': '10464',
	'Pomonok-Flushing Heights-Hillcrest': '11354',
	'Port Richmond': '10302',
	'Prospect Heights': '11238',
	'Queens Village': '11428',
	'Queensbridge-Ravenswood-Long Island City': '11106',
	'Rego Park': '11374',
	'Richmond Hill': '11418',
	'Ridgewood': '11385',
	'Rosedale': '11422',
	'Seagate-Coney Island': '11224',
	'Soundview-Bruckner': '10472',
	'Soundview-Castle Hill-Clason Point-Harding Pa': '10472',
	'South Jamaica': '11433',
	'South Ozone Park': '11436',
	'St. Albans': '11412',
	'Stapleton-Rosebank': '10305',
	'Starrett City': '11239',
	'Steinway': '11105',
	'Stuyvesant Heights nyc': '11233',
	'Sunset Park East': '11220',
	'Sunset Park West': '11220',
	'University Heights-Morris Heights': '10453',
	'Upper West Side': '10024',
	'Washington Heights North': '10033',
	'Washington Heights South': '10033',
	'West New Brighton-New Brighton-St. George': '10310',
	'Whitestone': '11357',
	'Williamsburg': '11211',
	'Windsor Terrace': '11215',
	'Woodhaven': '11421',
	'Woodlawn-Wakefield': '10466',
	'Woodside': '11377',
	'Yorkville nyc': '10128'
}

# add nbs not in list in order to manually insert zip
def insert_nbs(nb_list, zip_dict):
	missing_count = 0
	not_missing_count = 0
	for nb in nb_list:
		if nb not in zip_dict:
			missing_count += 1
			zip_dict[nb] = 'MISSING'
			print('MISSING: ', nb)
		not_missing_count += 1
	return (missing_count, not_missing_count, zip_dict)

# breaks up nb1-nb2 in neighborhoods, add to new dictionary
def nb_in_zip(nb_list, dictionary):
	new_dict = {}
	for nb in nb_list:
		if '-' in nb:
			nbs = nb.split('-')
			for item in nbs:
				if item in dictionary:
					new_dict[nb] = dictionary[item]
					break
		elif nb in dictionary:
			new_dict[nb] = dictionary[nb]

	return new_dict