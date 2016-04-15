import os
import pandas as pd
file_list = os.listdir('economic_csv_files/')

def economic(filename):
	economic_csv = pd.read_csv(filename, skiprows=[2,3], converters={'Unnamed: 1': lambda x: x.replace(',','')})
	indexed = economic_csv.set_index('2009-2013 ACS Economic Profile')

	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = indexed.index[0]
	neighborhood = neighborhood_string[23:]

	# ECONOMIC TABLE
	population_16_plus = int(indexed.loc['Population 16 years and over'][0])
	labor_force = int(indexed.loc['In labor force'].iloc[0,0])
	employed = int(indexed.loc['Employed'].iloc[0,0])
	unemployed = int(indexed.loc['Unemployed'].iloc[0,0])
	people_below_poverty = int(indexed.loc['Below poverty'].iloc[1,0])
	all_people = int(indexed.loc['All people'][0])

	HH_income_under_50 = sum([
		int(indexed.loc['Less than $10,000'].iloc[0,0]),
		int(indexed.loc['$10,000 to $14,999'].iloc[0,0]),
		int(indexed.loc['$15,000 to $24,999'].iloc[0,0]),
		int(indexed.loc['$25,000 to $34,999'].iloc[0,0]),
		int(indexed.loc['$35,000 to $49,999'].iloc[0,0])
	])

	HH_income_50_100 = sum([
		int(indexed.loc['$50,000 to $74,999'].iloc[0,0]),
		int(indexed.loc['$75,000 to $99,999'].iloc[0,0]),
	])

	HH_income_100_200 = sum([
		int(indexed.loc['$100,000 to $149,999'].iloc[0,0]),
		int(indexed.loc['$150,000 to $199,999'].iloc[0,0]),
		])

	HH_income_200_plus = int(indexed.loc['$200,000 or more'].iloc[0,0])

	HH_income_mean = int(indexed.loc['Mean household income (dollars)'][0])
	HH_income_median = int(indexed.loc['Median household income (dollars)'][0])

	total_households = int(indexed.loc['Total households'][0])

	

	
	economic_values = [
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
		"unemployment_rate",
		"below_poverty_rate",
		"HH_income_under_50_rate",
		"HH_income_50_100_rate",
		"HH_income_100_200_rate",
		"HH_income_200_plus_rate",
		"HH_income_median",
		"HH_income_mean"
	]

	economic_dictionary = dict(zip(economic_keys, economic_values))
	print(economic_dictionary)


for filename in file_list:
	economic(filename)

	"""
	set row 1 to index for new data frame. Note that word that will change should be Social 
	indexed = my_file.set_index('2009-2013 ACS Social Profile')

	turn string value associated with a label into integer
	total_households=int(indexed.loc['Total households'][0].replace(',',''))

	"""