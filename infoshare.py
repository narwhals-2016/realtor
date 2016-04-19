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
city_dict = {
	**bronx_dict,
	**brooklyn_dict,
	**manhattan_dict,
	**queens_dict,
	**staten_island_dict,
}