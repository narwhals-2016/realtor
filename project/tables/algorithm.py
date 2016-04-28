from tables.models import Ages, Demographic, Economic, UnitDescription, SchoolEducation, Building, Score, UnitValue
from pprint import pprint
from numpy import repeat
# expecting that Jack's tuples 
# will match up form's input results--not the keys but the values--
# with fields in the database. if not can make a dictionary here
# with those mappings, like the tables_map

# f is a mock form.clean_data
f = {
	'age': 'age_25_34', 'gender': 'gender_m', 
	'number_of_units': 'number_of_units_2_less',
	'ownership_type': 'resident_type_owner',
	'number_of_rooms': 'rooms_per_unit_over_4',
	'building_age': 'constructed_after_2000',
	'night_life_importance': 'night_life_score',
}

# 
tables_map = {
	'age': Ages,
	'gender': Demographic,
	'current_edu_level': SchoolEducation,
	'number_of_units': Building,
	'ownership_type': UnitDescription,
	'number_of_rooms': UnitDescription,
	'building_age': Building,
	'night_life_importance': Score,
	'noise_level_checkbox': Score,
	'crime_level_checkbox': Score,
	'income_level_range': Economic,
	'marital_status_checkbox': Demographic,
	'number_of_vehicles': UnitDescription,
	# 'number_of_children': ??,
	# 'price_range': UnitValue,
}

range_list = [
	'income_level_range',
	# 'price_range',
	# 'commute_time_range',
]

importance_fields_three_levels = {
	'night_life_importance': 'night_life_score',
}

importance_fields_two_levels = [
	'noise_level_checkbox',
	'crime_level_checkbox',
]


def put_value_in_group(key, value):
	if key == 'income_level_range':
		if 0 <= value < 50:
			result = 'income_0_50'
		elif 50 <= value < 100:
			result = 'income_50_100'
		elif 100 <= value < 200:
			result = 'income_100_200'
		elif value >= 200:
			result = 'income_200_plus'
	return result



def make_queries(form):
	ten_results = {}
	for key in form:
		# perform 'ten best' query for each key in form results #
		# if the form results mapping of choices in forms.py for 
		# SearchForm works, can just use form[key] for field
		if form[key] != 'empty':
			if key in tables_map:
				print('in tables_map', key)
				if key in range_list:
					print(form[key])
					field = put_value_in_group(key, int(form[key]))
					print('field result', field)
					ten_results[key] = sort_by_largest_to_smallest(table=tables_map[key], field=field)
				elif key in importance_fields_two_levels:
					print('INSIDE IMPORTANCE TWO FIELDS', key)
					ten_results[key] = sort_by_smallest_to_largest(table=tables_map[key], field=form[key])
				elif key in importance_fields_three_levels:
					print('INSIDE IMPORTANCE THREE FIELDS', key)
					if form[key] == 'high':
						print('INSIDE IMPORTANCE HIGH', key) 
						ten_results[key] = sort_by_smallest_to_largest(
							table=tables_map[key], field=importance_fields_three_levels[key]
						)
					elif form[key] == 'very_high':
						print('INSIDE IMPORTANCE VERY HIGH', key)
						nb_list = sort_by_smallest_to_largest(
							table=tables_map[key], field=importance_fields_three_levels[key]
						)
						new_list = repeat(nb_list, 2)
						ten_results[key] = new_list
				else:
					print('in ten results part', key)
					ten_results[key] = sort_by_largest_to_smallest(table=tables_map[key], field=form[key])
	return ten_results

def sort_by_largest_to_smallest(table, field):
	# '-' orders by descending
	return table.objects.order_by('-' + field)[:10]

def sort_by_smallest_to_largest(table, field):
	return table.objects.order_by(field)[:10]

def count_neighborhoods(results_dict):
	nb_counter = {} 
	for key in results_dict:
		# value of results_dict[key] is list of neighborhoods
		for result in results_dict[key]:
			# if that neighborhood already in nb_counter, increment by one
			if result.neighborhood.name in nb_counter:
				nb_counter[result.neighborhood.name] += 1
			else:
				# if not in nb_counter, add to nb_counter
				nb_counter[result.neighborhood.name] = 1
	# sorts least to greatest, returns array of tuples of neighborhood and count
	return nb_counter

def find_three_most_common(nb_dict):
	sorted_dict = sorted(nb_dict.items(), key = lambda x:x[1])
	# gets the last three, or the ones with the highest count
	three_most_common = sorted_dict[len(sorted_dict)-3:]
	# get list of neighborhood names
	print('common', three_most_common)
	three_neighborhoods = [nb[0] for nb in three_most_common]
	print('n', three_neighborhoods)
	return three_neighborhoods


def get_results(form_dict):
	# performs each query and gathers data
	query_results = make_queries(form_dict)
	print('query_results', query_results)
	# tally the neighborhoods in query results
	nb_count = count_neighborhoods(query_results)
	print('nb_count result', nb_count)
	return find_three_most_common(nb_count)
