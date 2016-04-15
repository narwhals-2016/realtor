import os
import pandas as pd
file_list = os.listdir('housing_csv_files/')



def housing(filename):
	housing_csv = pd.read_csv(filename, skiprows=[1,2,3], converters={'Unnamed: 1': lambda x: x.replace(',','')})
	indexed = housing_csv.set_index('2009-2013 ACS Housing Profile')

	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = indexed.index[0]
	neighborhood = neighborhood_string[23:]

	#################### unit-value table ######################
	# rent
	rent_1000_or_less = sum([
		int(indexed.loc['Less than $200'][0]),
		int(indexed.loc['$200 to $299'][0]),
		int(indexed.loc['$300 to $499'][0]),
		int(indexed.loc['$500 to $749'][0]),
		int(indexed.loc['$750 to $999'][0])
	])	

	rent_1000_to_1499 = int(indexed.loc['$1,000 to $1,499'][0])
	rent_1500_or_more = int(indexed.loc['$1,500 or more'][0])

	median_dollars_df = indexed.loc['Median (dollars)'] 
	rent_median = float(median_dollars_df.iloc[1,0])
	total_rental_units = int(indexed.loc['Occupied units paying rent'][0])

	# owned
	owned_unit_500k_or_less = sum([
		int(indexed.loc['Less than $50,000'][0]),
		int(indexed.loc['$50,000 to $99,999'][0]),
		int(indexed.loc['$100,000 to $149,999'][0]),
		int(indexed.loc['$150,000 to $199,999'][0]),
		int(indexed.loc['$200,000 to $299,999'][0]),
		int(indexed.loc['$300,000 to $499,999'][0]) 
	])

	owned_five_hundred_thousand_to_one_million = int(indexed.loc['$500,000 to $999,999'][0])
	owned_one_million_or_more = int(indexed.loc['$1,000,000 or more'][0])
	owned_median = float(median_dollars_df.iloc[0,0])
	owner_occupied_units_df = indexed.loc['Owner-occupied units'] 
	total_owned_units = int(owner_occupied_units_df.iloc[0,0])

	rental_values = [
		round(rent_1000_or_less/total_rental_units,2),
		round(rent_1000_to_1499/total_rental_units,2),
		round(rent_1500_or_more/total_rental_units,2),
		rent_median,	  
	]

	rental_keys = [
		"rent_1000_or_less",
		"rent_1000_to_1499",
		"rent_1500_or_more",
		"rent_median",
	]

	owned_values = [
		round(owned_unit_500k_or_less/total_owned_units,2),
		round(owned_five_hundred_thousand_to_one_million/total_owned_units,2),
		round(owned_one_million_or_more/total_owned_units,2),
		owned_median,	
	]

	owned_keys = [
		"owned_unit_500k_or_less",
		"owned_five_hundred_thousand_to_one_million",
		"owned_one_million_or_more",
		"owned_median",
	]

	rental_dictionary = dict(zip(rental_keys, rental_values))
	owned_dictionary = dict(zip(owned_keys, owned_values))

	print(neighborhood, rental_dictionary)
	print(neighborhood, owned_dictionary)
	#####################unit value######################
	##############unit data table################
	# total below used for unit data and building table total
	total_units_df = indexed.loc['Total housing units'] 
	total_units = int(total_units_df.iloc[0,0])

	total_occupied_units_df = indexed.loc['Occupied housing units'] 
	total_occupied_units = int(total_occupied_units_df.iloc[0,0])

	occupied_units = int(indexed.loc['Occupied housing units'][0])
	vacant_units = int(indexed.loc['Vacant housing units'][0])

	rooms_3_or_less = sum([
		int(indexed.loc['1 room']),
		int(indexed.loc['2 room']),
		int(indexed.loc['3 room']),
	])
	rooms_4_or_more = sum([
		int(indexed.loc['4 room']),
		int(indexed.loc['5 room']),
		int(indexed.loc['6 room']),
		int(indexed.loc['7 room']),
		int(indexed.loc['8 room']),
		int(indexed.loc['9 rooms or more']),
	])
	rooms_median = int(indexed.loc['Median rooms'])

	resident_type_owner = int(indexed.loc['Owner-occupied'][0])
	resident_type_renter = int(indexed.loc['Renter-occupied'][0])

	moved_in_since_2010 = int(indexed.loc['Moved in 2010 or later'][0])
	moved_in_2000_2009 = int(indexed.loc['Moved in 2000 to 2009'][0])
	moved_in_before_2000 = sum([
		int(indexed.loc['Moved in 1990 to 1999'][0]),
		int(indexed.loc['Moved in 1980 to 1989'][0]),
		int(indexed.loc['Moved in 1970 to 1979'][0]),
		int(indexed.loc['Moved in 1969 or earlier'][0]),
	])

	vehicles_zero = int(indexed.loc['No vehicles available'])
	vehicles_at_least_one = sum([
		int(indexed.loc['1 vehicle available'][0]),
		int(indexed.loc['2 vehicle available'][0]),
		int(indexed.loc['3 or more vehicles available'][0]),
	])


	# BUILDING
	units_2_or_less = sum([
		int(indexed.loc['1-unit, detached'][0]),
		int(indexed.loc['1-unit, attached'][0]),
		int(indexed.loc['2 units'][0]),
	])

	units_3_9 = sum([
		int(indexed.loc['3 or 4 units'][0]),
		int(indexed.loc['5 to 9 units'][0]),
	])

	units_10_plus = sum([
		int(indexed.loc['10 to 19 units'][0]),
		int(indexed.loc['20 or more units'][0]),
	])

	constructed_before_1970 = sum([
		int(indexed.loc['Built 1939 or earlier'][0]),
		int(indexed.loc['Built 1940 to 1949'][0]),
		int(indexed.loc['Built 1950 to 1959'][0]),
		int(indexed.loc['Built 1960 to 1969'][0]),
	])

	constructed_1970_to_2000 = sum([
		int(indexed.loc['Built 1970 to 1979'][0]),
		int(indexed.loc['Built 1980 to 1989'][0]),
		int(indexed.loc['Built 1990 to 1999'][0]),
	])

	constructed_after_2000 = sum([
		int(indexed.loc['Built 2000 to 2009'][0]),
		int(indexed.loc['Built 2010 or later'][0]),
	])

for filename in file_list:
	housing(filename)

