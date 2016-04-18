import os
import pandas as pd
from tables.models import Neighborhood, Economic 


def economic(filename):
	economic_file = pd.read_excel(filename, skiprows=[2,3])
	# may only need converters when reading csv; possible that excel file reads in as numbers
	# converters={'Unnamed: 1': lambda x: x.replace(',','')}
	indexed = economic_file.set_index('2009-2013 ACS Economic Profile')

	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = indexed.index[0]
	neighborhood = neighborhood_string[23:]

	# seed neighborhood table first; only use if neighborhoods have not been seeded yet
	# neighborhood_obj = Neighborhood.objects.create(name=neighborhood)

	# option if neighborhood already in table:
	neigborhood_obj = Neighborhood.objects.get(name=neighborhood) 

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
		round(labor_force/population_16_plus,2),
		round(unemployed/labor_force,2),
		round(people_below_poverty/all_people,2),
		round(HH_income_under_50/total_households,2),
		round(HH_income_50_100/total_households,2),
		round(HH_income_100_200/total_households,2),
		round(HH_income_200_plus/total_households,2),
		HH_income_median,
		HH_income_mean
	]

	economic_keys =[
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
		neighborhood=neighborhood_obj,
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
def run(folder):
	file_list = os.listdir(folder)
	for filename in file_list:
		economic(folder + filename)

	"""
	set row 1 to index for new data frame. Note that word that will change should be Social 
	indexed = my_file.set_index('2009-2013 ACS Social Profile')

	turn string value associated with a label into integer
	total_households=indexed.loc['Total households'][0].replace(',','')

	"""