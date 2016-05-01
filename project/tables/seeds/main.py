from . import (
	load_neighborhoods, housing_load, economic_load, 
	demographic_load, schools_csv, social_csv,crime,
	nightlife, noise, crime, google_distance_api
)

def seed_db(data_path, *seed_tables):
	# creates neighborhoods
	if "all" in seed_tables:
		# waiting for GOOGLE_KEY to add "commute"
		seed_tables = ["neighborhoods","housing","crime","economic","social", "demographic", "nightlife", "noise", "commute"]

	if "neighborhoods" in seed_tables:
		load_neighborhoods.run(data_path, 'housing')
		load_neighborhoods.run(data_path, 'housing_temp')
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

	if "crime" in seed_tables:
		crime.run()
		print ("\n *** crime done *** \n")


