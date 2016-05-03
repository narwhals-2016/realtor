"""
only table to add is Economic
>>> from tables.economic_load import run
>>> run(folder)
"""

import os
import pandas as pd
from tables.models import Neighborhood, Economic 

def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3], sheetname=0)
	indexed = housing_file.set_index('2009-2013 ACS Economic Profile')
	return indexed

def get_neighborhood_name(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	return neighborhood_string[23:]
	
def get_neighborhood_obj(neighborhood):	
	# option if neighborhood already in table:
	print('in get_neighborhood_obj', neighborhood)
	return Neighborhood.objects.get(name=neighborhood)

def make_economic_row(indexed, neighborhood):
	print('nb: ', neighborhood.name)
	# ECONOMIC TABLE: locate values, sum where needed, and turn strings into numbers
	all_people = indexed.loc['All people'][0]
	population_16_plus = indexed.loc['Population 16 years and over'][0]
	labor_force = indexed.loc['In labor force'].iloc[0,0]
	employed = indexed.loc['Employed'].iloc[0,0]
	unemployed = indexed.loc['Unemployed'].iloc[0,0]
	people_below_poverty = indexed.loc['Below poverty'].iloc[1,0]

	total_households = indexed.loc['Total households'][0]
	
	HH_income_under_50 = sum([
		indexed.loc['Less than $10,000'].iloc[0,0],
		indexed.loc['$10,000 to $14,999'].iloc[0,0],
		indexed.loc['$15,000 to $24,999'].iloc[0,0],
		indexed.loc['$25,000 to $34,999'].iloc[0,0],
		indexed.loc['$35,000 to $49,999'].iloc[0,0],
	])

	HH_income_50_100 = sum([
		indexed.loc['$50,000 to $74,999'].iloc[0,0],
		indexed.loc['$75,000 to $99,999'].iloc[0,0],
	])

	HH_income_100_200 = sum([
		indexed.loc['$100,000 to $149,999'].iloc[0,0],
		indexed.loc['$150,000 to $199,999'].iloc[0,0],
		])

	HH_income_200_plus = indexed.loc['$200,000 or more'].iloc[0,0]

	HH_income_mean = indexed.loc['Mean household income (dollars)'][0]
	HH_income_median = indexed.loc['Median household income (dollars)'][0]

	economic_values = [
		round((labor_force/population_16_plus)*100,2),
		round((unemployed/labor_force)*100,2),
		round((people_below_poverty/all_people)*100,2),
		round((HH_income_under_50/total_households)*100,2),
		round((HH_income_50_100/total_households)*100,2),
		round((HH_income_100_200/total_households)*100,2),
		round((HH_income_200_plus/total_households)*100,2),
		HH_income_median,
		HH_income_mean
	]

	economic_keys = [
		"labor_force_rate",
		"unemployment_rate",
		"below_poverty_rate",
		"HH_income_under_50_rate",
		"HH_income_50_100_rate",
		"HH_income_100_200_rate",
		"HH_income_200_plus_rate",
		"HH_income_median",
		"HH_income_mean",
	]

	econ_dict = dict(zip(economic_keys, economic_values))

	# make economic table object, now that we have neighborhood object and values have been converted to rates where necessary
	economic_obj = Economic.objects.create(
		neighborhood=neighborhood,
		laborforce=econ_dict["labor_force_rate"],
        unemployed=econ_dict["unemployment_rate"],
        below_poverty_level=econ_dict["below_poverty_rate"],
        income_0_50=econ_dict["HH_income_under_50_rate"],
        income_50_100=econ_dict["HH_income_50_100_rate"], 
        income_100_200=econ_dict["HH_income_100_200_rate"],
        income_200_plus=econ_dict["HH_income_200_plus_rate"],
        median_income=econ_dict["HH_income_median"],
        mean_income=econ_dict["HH_income_mean"],
	)

def run(folder_path, folder):
	file_list = os.listdir(folder_path + folder)
	for filename in file_list:
		# use pandas to get dataframe from xlsx file
		dataframe = parse_file(folder_path + folder + '/' + filename)
		# identify neighborhood
		neighborhood = get_neighborhood_name(dataframe)
		if neighborhood == "Rikers Island":
			print('Rikers Island blank and pass **********')
			continue
		else:
			neighborhood = get_neighborhood_obj(neighborhood)
			make_economic_row(dataframe, neighborhood)
	print('DONE')