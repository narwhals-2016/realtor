import time
from . import (
	load_neighborhoods, load_geocodes, load_missing_geocodes,
	load_pic_urls, load_streetviews, housing_load, economic_load, 
	demographic_load, schools_csv, social_csv,crime,
	nightlife, noise, crime, google_distance_api
)

'''
from tables.seeds import seed_db

seed_db("tables/seeds/datasets/", "all")
'''


def seed_db(data_path, *seed_tables):
# open a log file to capture prints as the data is loaded- this will be helpful to 
# debug seeding problems
	timestr = time.strftime("%Y%m%d-%H%M%S")
	f = open(data_path+'log_file'+timestr+'.txt', 'w')

	# creates neighborhoods
	if "all" in seed_tables:
		# waiting for GOOGLE_KEY to add "commute"
		seed_tables = ["neighborhoods","housing","crime","economic","social", "demographic", "nightlife", "schools", "noise", "commute"]

	if "neighborhoods" in seed_tables:
		load_neighborhoods.run(data_path, 'housing')
		load_neighborhoods.run(data_path, 'housing_temp')
		load_geocodes.run()
		load_missing_geocodes.run()
		load_streetviews.run()
		print ("\n *** neighborhoods done *** \n")

	# loads housing data
	if "housing" in seed_tables:
		housing_load.run(data_path, 'housing', 'all')
		housing_load.run(data_path, 'housing_temp', 'all')
		print ("\n *** housing done *** \n")

	# loads economic data
	if "economic" in seed_tables:
		economic_load.run(data_path, 'econ')
		economic_load.run(data_path, 'econ_temp')
		print ("\n *** economic done *** \n")

	# loads social data (must run before demographic data)
	if "social" in seed_tables:
		social_csv.run(data_path, 'social')
		social_csv.run(data_path, 'social_temp')
		print ("\n *** social done *** \n")

	# loads demographic data
	if "demographic" in seed_tables:
		demographic_load.run(data_path, 'demographic', 'all')
		demographic_load.run(data_path, 'demo_temp', 'all')
		print ("\n *** demographic done *** \n")

	# loads school data
	if "schools" in seed_tables:
		schools_csv.run(data_path + "schools/")
		print ("\n *** school done *** \n")

	# nightlife complete
	if "nightlife" in seed_tables:
		nightlife.run()
		print ("\n *** nightlife done *** \n")

	# loads noise data
	if "noise" in seed_tables:
		noise.run()
		print ("\n *** noise done *** \n")

	# loads commute data
	if "commute" in seed_tables:
		google_distance_api.run()
		print ("\n *** commute done *** \n")

	# loads crime data
	if "crime" in seed_tables:
		crime.run()
		print ("\n *** crime done *** \n")


