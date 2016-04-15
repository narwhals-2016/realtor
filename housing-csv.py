import pandas as pd

housing_csv = pd.read_csv('housing-middle-village.csv', skiprows=[1,2,3], converters={'Unnamed: 1': lambda x: x.replace(',','')})

print(housing_csv)
indexed = housing_csv.set_index('2009-2013 ACS Housing Profile')

# two_units_or_less = fuck('1-unit, detached')+fuck('1-unit, attached') + fuck('2-units')
# # 	int(indexed.loc['1-unit, detached'][0].replace(',','')) +
# # 	int(indexed.loc['1-unit, attached'][0].replace(',','')) +
# # 	int(indexed.loc['2 units'][0].replace(',',''))
# print(two_units_or_less)

# unit-value table
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

print(rental_dictionary)
print(owned_dictionary)

# resident_type_owner = int(indexed.loc['owner-occupied'][0]),

