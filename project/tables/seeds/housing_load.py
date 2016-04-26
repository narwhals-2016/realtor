"""
Script to load census housing data into django models
add one table at a time; current tables and their run function parameter strings: "all", "building", "unit_value", "unit_description"
>>> from tables.housing_load import run
>>> run(folder, table)

"""

import os
import pandas as pd
from tables.models import Neighborhood, Building, UnitValue, UnitDescription


def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3], sheetname=0)
	indexed = housing_file.set_index('2009-2013 ACS Housing Profile')
	return indexed

def	get_neighborhood(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	neighborhood = neighborhood_string[23:]
	# option if neighborhood already in table:
	print('in get_neighborhood', neighborhood)
	neigborhood_obj = Neighborhood.objects.get(name=neighborhood)
	return neigborhood_obj
	
def make_building_row(dataframe, neighborhood):
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
	building_values = [
		round((units_2_or_less/total_housing_units)*100, 2),
		round((units_3_9/total_housing_units)*100, 2),
		round((units_10_plus/total_housing_units)*100, 2),
		round((constructed_before_1970/total_housing_units)*100, 2),
		round((constructed_1970_to_2000/total_housing_units)*100, 2),
		round((constructed_after_2000/total_housing_units)*100, 2),
	]

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


	owned_values = [
		round((owned_unit_500k_or_less/total_owned_units)*100,2),
		round((owned_five_hundred_thousand_to_one_million/total_owned_units)*100,2),
		round((owned_one_million_or_more/total_owned_units)*100,2),
		owned_median,	
	]

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

	rental_values = [
		round((rent_1000_or_less/total_rental_units)*100,2),
		round((rent_1000_to_1499/total_rental_units)*100,2),
		round((rent_1500_or_more/total_rental_units)*100,2),
		rent_median,	  
	]
	
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

def make_unit_description_row(dataframe, nb):
	##############unit data table################
	# total below used for unit data and building table total
	total_units_df = dataframe.loc['Total housing units'] 
	total_units = total_units_df.iloc[0,0]

	total_occupied_units_df = dataframe.loc['Occupied housing units'] 
	occupied_units = total_occupied_units_df.iloc[0,0]
	vacant_units = dataframe.loc['Vacant housing units'][0]

	rooms_3_or_less = sum([
		dataframe.loc['1 room'][0],
		dataframe.loc['2 room'][0],
		dataframe.loc['3 room'][0],
	])
	rooms_4_or_more = sum([
		dataframe.loc['4 room'][0],
		dataframe.loc['5 room'][0],
		dataframe.loc['6 room'][0],
		dataframe.loc['7 room'][0],
		dataframe.loc['8 room'][0],
		dataframe.loc['9 rooms or more'][0],
	])
	rooms_median = dataframe.loc['Median rooms'][0]

	resident_type_owner = dataframe.loc['Owner-occupied'][0]
	resident_type_renter = dataframe.loc['Renter-occupied'][0]

	moved_in_since_2010 = dataframe.loc['Moved in 2010 or later'][0]
	moved_in_2000_2009 = dataframe.loc['Moved in 2000 to 2009'][0]
	moved_in_before_2000 = sum([
		dataframe.loc['Moved in 1990 to 1999'][0],
		dataframe.loc['Moved in 1980 to 1989'][0],
		dataframe.loc['Moved in 1970 to 1979'][0],
		dataframe.loc['Moved in 1969 or earlier'][0],
	])

	vehicles_zero = dataframe.loc['No vehicles available'][0]
	vehicles_at_least_one = sum([
		dataframe.loc['1 vehicle available'][0],
		dataframe.loc['2 vehicles available'][0],
		dataframe.loc['3 or more vehicles available'][0],
	])

	unit_description_obj = UnitDescription.objects.create(
		neighborhood =nb,
		units_occupied = round((occupied_units/total_units)*100,2),
		units_vacant = round((vacant_units/total_units)*100,2),
		rooms_per_unit_under_3 = round((rooms_3_or_less/total_units)*100,2),
		rooms_per_unit_over_4 = round((rooms_4_or_more/total_units)*100,2),
		resident_type_owner = round((resident_type_owner/occupied_units)*100,2),
		resident_type_renter = round((resident_type_renter/occupied_units)*100,2),
		length_residence_before_2000 = round((moved_in_before_2000/occupied_units)*100,2),
		length_residence_2000_2009 = round((moved_in_2000_2009/occupied_units)*100,2),
		length_residence_after_2010 = round((moved_in_since_2010/occupied_units)*100,2),
		vehicles_0 = round((vehicles_zero/occupied_units)*100,2),
		vehicles_1_plus = round((vehicles_at_least_one/occupied_units)*100,2),
		rooms_median = rooms_median,
	)

def run(folder_path, folder, table):
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
		elif table == "building":
			make_building_row(dataframe, neighborhood)
		elif table == "unit_value":
			make_unit_value_row(dataframe, neighborhood)
		elif table == "unit_description":
			make_unit_description_row(dataframe, neighborhood)
		elif table == "all":
			make_building_row(dataframe, neighborhood)
			make_unit_value_row(dataframe, neighborhood)
			make_unit_description_row(dataframe, neighborhood)
	print('DONE')




