"""
script to load directory of census files into django tables.
"""

import os
import pandas as pd
from tables.models import Neighborhood, Ages

def demo(filename):
	demo_excel = pd.read_excel(filename, skiprows=[2,3])
	# converters parameter not needed for read_excel with xlsx files; column already interpreted as integers
	# converters={'Unnamed: 1': lambda x: x.replace(',','')}
	indexed = demo_excel.set_index('2009-2013 ACS Demographic Profile')

	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = indexed.index[0]
	neighborhood = neighborhood_string[23:]

	# option if neighborhood already in table:
	print('string: ', neighborhood)
	neighborhood_obj = Neighborhood.objects.get(name=neighborhood) 
	print('nb_obj: ', neighborhood_obj)
	# AGE 
	under_nineteen = sum([
		indexed.loc['Under 5 years'][0],
		indexed.loc['5 to 9 years'][0],
		indexed.loc['10 to 14 years'][0],
		indexed.loc['15 to 19 years'][0]
	])

	twenty_to_twentyfour = indexed.loc['20 to 24 years'][0]
	twentyfive_to_thirtyfour = indexed.loc['25 to 34 years'][0]

	thirtyfive_to_sixtyfour = sum([
		indexed.loc['35 to 44 years'][0],
		indexed.loc['45 to 54 years'][0],
		indexed.loc['55 to 59 years'][0],
		indexed.loc['60 to 64 years'][0]
	])

	over_sixtyfive = sum([
		indexed.loc['65 to 74 years'][0],
		indexed.loc['75 to 84 years'][0],
		indexed.loc['85 years and over'][0]
	])

	age_median = indexed.loc['Median age (years)'][0]


	# returns dataframe
	pop_df = indexed.loc['Total population']
	# total pop value is in top left cell
	total_population = pop_df.iloc[0,0]

	if total_population != 0:
		age_values = [
			round(under_nineteen/total_population,2), 
			round(twenty_to_twentyfour/total_population,2), 
			round(twentyfive_to_thirtyfour/total_population,2), 
			round(thirtyfive_to_sixtyfour/total_population,2), 
			round(over_sixtyfive/total_population,2),
			age_median,  
		]
	else:
		age_values = [0,0,0,0,0,0]

	age_keys = [
		"under_nineteen", 
		"twenty_to_twentyfour", 
		"twentyfive_to_thirtyfour", 
		"thirtyfive_to_sixtyfour", 
		"over_sixtyfive",  
		"age_median",
	]

	age_dict = dict(zip(age_keys, age_values))

	age_obj = Ages.objects.create(
		neighborhood=neighborhood_obj,
		age_0_19=age_dict["under_nineteen"],
        age_20_24=age_dict["twenty_to_twentyfour"],
        age_25_34=age_dict["twentyfive_to_thirtyfour"],
        age_35_64=age_dict["thirtyfive_to_sixtyfour"],
        age_65_over=age_dict["over_sixtyfive"],
        age_median=age_dict["age_median"], 
	)
	print('made age_obj')	
	# GENDER
	male_df = indexed.loc['Male']
	male = male_df.iloc[0,0]

	female_df = indexed.loc['Female']
	female = female_df.iloc[0,0]

	if total_population != 0:
		gender_values = [
			round(male/total_population,2),
			round(female/total_population,2), 
		]
	else:
		gender_values = [0,0]

	gender_keys =[
		"male",
		"female",
	]

	gender_dictionary = dict(zip(gender_keys, gender_values))


def run_demo(folder):
	file_list = os.listdir('tables/datasets/' + folder)
	for filename in file_list:
		demo('tables/datasets/' + folder + '/' + filename)