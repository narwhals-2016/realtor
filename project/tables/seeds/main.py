from . import (
	load_neighborhoods, housing_load, economic_load, 
	demographic_load, schools_csv, social_csv,
	nightlife, noise
)

def seed_db(data_path, *seed_tables):
	# creates neighborhoods
	if "all" in seed_tables:
		seed_tables = [
			"neighborhoods","housing","economic",
			"social", "demographic", "schools", "nightlife", "noise"
		]
	if "neighborhoods" in seed_tables:
		load_neighborhoods.run(data_path, 'housing')
		load_neighborhoods.run(data_path, 'housing_temp')
	# loads housing data
	if "housing" in seed_tables:
		housing_load.run(data_path, 'housing', 'all')
		housing_load.run(data_path, 'housing_temp', 'all')
	# loads economic data
	if "economic" in seed_tables:
		economic_load.run(data_path, 'econ')
		economic_load.run(data_path, 'econ_temp')
	# loads social data (must run before demographic data)
	if "social" in seed_tables:
		social_csv.run(data_path, 'social')
		social_csv.run(data_path, 'social_temp')
	# loads demographic data
	if "demographic" in seed_tables:
		demographic_load.run(data_path, 'demographic', 'all')
		demographic_load.run(data_path, 'demo_temp', 'all')
	# loads school data
	if "schools" in seed_tables:
		schools_csv.run(data_path + "schools/")
	# nightlife not complete
	if "nightlife" in seed_tables:
		nightlife.run()
	# loads noise data
	if "noise" in seed_tables:
		noise.run()



