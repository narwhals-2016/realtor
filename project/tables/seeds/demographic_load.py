"""
script to load directory of demographic census files into django tables.
add one table at a time; current tables and their run function parameter strings: "ages", "demo_gender", "all"
demo_gender adds gender data to already existing Demographic rows, which are loaded via social files in social_csv.py
>>> from tables.demographic_load import run
>>> run(folder, table)
"""

import os
import pandas as pd
from tables.models import Neighborhood, Ages, Demographic

def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3], sheetname=0)
	indexed = housing_file.set_index('2009-2013 ACS Demographic Profile')
	return indexed

def	get_neighborhood(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	neighborhood = neighborhood_string[23:]
	# option if neighborhood already in table:
	print('in get_neighborhood', neighborhood)
	neigborhood_obj = Neighborhood.objects.get(name=neighborhood)
	return neigborhood_obj
	


def make_ages_row(indexed, neighborhood):
	print('nb_obj: ', neighborhood.name)
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

	# returns a dataframe
	pop_df = indexed.loc['Total population']
	# total pop value is in top left cell
	total_population = pop_df.iloc[0,0]

	age_values = [
		round((under_nineteen/total_population)*100,2), 
		round((twenty_to_twentyfour/total_population)*100,2), 
		round((twentyfive_to_thirtyfour/total_population)*100,2), 
		round((thirtyfive_to_sixtyfour/total_population)*100,2), 
		round((over_sixtyfive/total_population)*100,2),
		age_median,  
	]

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
		neighborhood=neighborhood,
		age_0_19=age_dict["under_nineteen"],
        age_20_24=age_dict["twenty_to_twentyfour"],
        age_25_34=age_dict["twentyfive_to_thirtyfour"],
        age_35_64=age_dict["thirtyfive_to_sixtyfour"],
        age_65_over=age_dict["over_sixtyfive"],
        age_median=age_dict["age_median"], 
	)
	
# GENDER
# not complete
def add_gender_to_demographic_row(indexed, neighborhood):
	print('nb_obj: ', neighborhood.name)
	
	pop_df = indexed.loc['Total population']
	# total pop value is in top left cell
	total_population = pop_df.iloc[0,0]

	male_df = indexed.loc['Male']
	male = male_df.iloc[0,0]

	female_df = indexed.loc['Female']
	female = female_df.iloc[0,0]

	gender_values = [
		round((male/total_population)*100,2),
		round((female/total_population)*100,2), 
	]

	gender_keys =[
		"male",
		"female",
	]
	
	gender_dict = dict(zip(gender_keys, gender_values))
	demographic_row = Demographic.objects.get(neighborhood=neighborhood)
	demographic_row.gender_m = gender_dict['male']
	demographic_row.gender_f = gender_dict['female']
	demographic_row.save()
	print("SAVED")

def run(folder_path, folder, table):
	# 'tables/datasets/' 
	file_list = os.listdir(folder_path + folder)
	for filename in file_list:
		# use pandas to get dataframe from xlsx file
		dataframe = parse_file(folder_path + folder + '/' + filename)
		# identify neighborhood
		neighborhood = get_neighborhood(dataframe)
		# which table tree
		# if rikers don't add to table
		if neighborhood.name == "Rikers Island":
			print('Rikers Island blank and pass')
		elif table == "ages":
			make_ages_row(dataframe, neighborhood)
		elif table == "demo_gender":
			add_gender_to_demographic_row(dataframe, neighborhood)
		elif table == "all":
			make_ages_row(dataframe, neighborhood)
			add_gender_to_demographic_row(dataframe, neighborhood)
	print('DONE')