"""
Script to load census housing data into django models
from tables.housing_load import run_buildings
run_buildings()
"""

import os
import pandas as pd
from tables.models import Neighborhood, Building, UnitValue 


def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3])
	indexed = housing_file.set_index('2009-2013 ACS Housing Profile')
	return get_neighborhood(indexed)

def	get_neighborhood(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	neighborhood = neighborhood_string[23:]
	# option if neighborhood already in table:
	print('in get_neighborhood', neighborhood)
	neigborhood_obj = Neighborhood.objects.get(name=neighborhood)
	return build_table_rows(dataframe, neigborhood_obj)
	
def build_table_rows(dataframe, nb):
	# get totals
	# total below used for unit description and building table total
	# note that both units per building and unit construction date are divided into to total housing units per neighborhood
	total_housing_units_df = dataframe.loc['Total housing units'] 
	total_housing_units = total_housing_units_df.iloc[0,0]
	total_occupied_units_df = dataframe.loc['Occupied housing units'] 
	total_occupied_units = total_occupied_units_df.iloc[0,0]
	vacant_units = dataframe.loc['Vacant housing units'][0]

	# make_building_row(dataframe, nb)
	if nb.name != "Rikers Island":
		make_unit_value_row(dataframe, nb)
	else:
		print('rikers blank')
	# make_unit_description_row(dataframe, nb, total_housing_units)
	
def make_building_row(dataframe, neighborhood):
	print('in make_building_row', neighborhood.name)
	# make building object in table
	total_housing_units_df = dataframe.loc['Total housing units'] 
	total_housing_units = total_housing_units_df.iloc[0,0]
	# get values
	units_2_or_less = sum([
		dataframe.loc['1-unit, detached'][0],
		dataframe.loc['1-unit, attached'][0],
		dataframe.loc['2 units'][0],
	])

	units_3_9 = sum([
		dataframe.loc['3 or 4 units'][0],
		dataframe.loc['5 to 9 units'][0],
	])

	units_10_plus = sum([
		dataframe.loc['10 to 19 units'][0],
		dataframe.loc['20 or more units'][0],
	])

	constructed_before_1970 = sum([
		dataframe.loc['Built 1939 or earlier'][0],
		dataframe.loc['Built 1940 to 1949'][0],
		dataframe.loc['Built 1950 to 1959'][0],
		dataframe.loc['Built 1960 to 1969'][0],
	])

	constructed_1970_to_2000 = sum([
		dataframe.loc['Built 1970 to 1979'][0],
		dataframe.loc['Built 1980 to 1989'][0],
		dataframe.loc['Built 1990 to 1999'][0],
	])

	constructed_after_2000 = sum([
		dataframe.loc['Built 2000 to 2009'][0],
		dataframe.loc['Built 2010 or later'][0],
	])

	# turn values into percentages, which will be passed into dictionary for seeding
	# need condition for if denominator total is zero. Implies 
	if total_housing_units != 0:
		building_values = [
			round(units_2_or_less/total_housing_units, 2),
			round(units_3_9/total_housing_units, 2),
			round(units_10_plus/total_housing_units, 2),
			round(constructed_before_1970/total_housing_units, 2),
			round(constructed_1970_to_2000/total_housing_units, 2),
			round(constructed_after_2000/total_housing_units, 2),
		]
	else:
		building_values = [0,0,0,0,0,0]

	building_keys = [
		"units_2_or_less",
		"units_3_9",
		"units_10_plus",
		"constructed_before_1970",
		"constructed_1970_to_2000",
		"constructed_after_2000",
	]

	building_dict = dict(zip(building_keys, building_values))

	# create building object in Django models
	building_obj = Building.objects.create(
		neighborhood=neighborhood,
		number_of_units_2_less=building_dict['units_2_or_less'],
		number_of_units_3_10=building_dict['units_3_9'],
		number_of_units_10_plus=building_dict['units_10_plus'],
		constucted_before_1970=building_dict['constructed_before_1970'],
		constucted_1970_2000=building_dict['constructed_1970_to_2000'],
		constucted_after_2000=building_dict['constructed_after_2000'], 
	)
	print("made building row")

def make_unit_value_row(dataframe, nb):	
	# owned
	owner_occupied_units_df = dataframe.loc['Owner-occupied units'] 
	total_owned_units = owner_occupied_units_df.iloc[0,0]
	
	owned_unit_500k_or_less = sum([
		dataframe.loc['Less than $50,000'][0],
		dataframe.loc['$50,000 to $99,999'][0],
		dataframe.loc['$100,000 to $149,999'][0],
		dataframe.loc['$150,000 to $199,999'][0],
		dataframe.loc['$200,000 to $299,999'][0],
		dataframe.loc['$300,000 to $499,999'][0] 
	])

	owned_five_hundred_thousand_to_one_million = dataframe.loc['$500,000 to $999,999'][0]
	owned_one_million_or_more = dataframe.loc['$1,000,000 or more'][0]
	median_dollars_df = dataframe.loc['Median (dollars)'] 
	owned_median = median_dollars_df.iloc[0,0]
	owner_occupied_units_df = dataframe.loc['Owner-occupied units'] 
	total_owned_units = owner_occupied_units_df.iloc[0,0]

	if total_owned_units != 0:
		owned_values = [
			round(owned_unit_500k_or_less/total_owned_units,2),
			round(owned_five_hundred_thousand_to_one_million/total_owned_units,2),
			round(owned_one_million_or_more/total_owned_units,2),
			owned_median,	
		]
	else:
		owned_values = [0,0,0,0]

	owned_keys = [
		"owned_unit_500k_or_less",
		"owned_five_hundred_thousand_to_one_million",
		"owned_one_million_or_more",
		"owned_median",
	]

	owned_dict = dict(zip(owned_keys, owned_values))

	# get rental values
	total_rental_units = dataframe.loc['Occupied units paying rent'][0]
	rent_1000_or_less = sum([
		dataframe.loc['Less than $200'][0],
		dataframe.loc['$200 to $299'][0],
		dataframe.loc['$300 to $499'][0],
		dataframe.loc['$500 to $749'][0],
		dataframe.loc['$750 to $999'][0]
	])	

	rent_1000_to_1499 = dataframe.loc['$1,000 to $1,499'][0]
	rent_1500_or_more = dataframe.loc['$1,500 or more'][0]

	median_dollars_df = dataframe.loc['Median (dollars)'] 
	rent_median = median_dollars_df.iloc[1,0]
	total_rental_units = dataframe.loc['Occupied units paying rent'][0]

	if total_rental_units != 0:
		rental_values = [
			round(rent_1000_or_less/total_rental_units,2),
			round(rent_1000_to_1499/total_rental_units,2),
			round(rent_1500_or_more/total_rental_units,2),
			rent_median,	  
		]
	else:
		rental_values = [0,0,0,0]
	
	rental_keys = [
		"rent_1000_or_less",
		"rent_1000_to_1499",
		"rent_1500_or_more",
		"rent_median",
	]
	rental_dict = dict(zip(rental_keys, rental_values))

	# make unit_value obj in UnitValue django table
	unit_value_obj = UnitValue.objects.create(
		neighborhood=nb,
		value_of_unit_500_less=owned_dict['owned_unit_500k_or_less'],
		value_of_unit_500_1M=owned_dict['owned_five_hundred_thousand_to_one_million'],
		value_of_unit_1M_plus=owned_dict['owned_one_million_or_more'],
		value_of_unit_median=owned_dict['owned_median'],
		gross_rent_1000_less=rental_dict['rent_1000_or_less'],
		gross_rent_1000_1500=rental_dict['rent_1000_to_1499'],
		gross_rent_1500_plus=rental_dict['rent_1500_or_more'],
		gross_rent_median=rental_dict['rent_median'],
	)

def run_buildings(folder):
	file_list = os.listdir('tables/datasets/' + folder)
	for filename in file_list:
		parse_file('tables/datasets/' + folder + '/' + filename)



