from tables.models import Ages, Demographic, Economic, UnitDescription, SchoolEducation, Building, Score
from pprint import pprint

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
}


def make_queries(form):
	ten_results = {}
	for key in form:
		# perform 'ten best' query for each key in form results #
		# if the form results mapping of choices in forms.py for 
		# SearchForm works, can just use form[key] for field
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
	three_neighborhoods = [nb[0] for nb in three_most_common]
	return three_neighborhoods


def get_results(form_dict):
	# performs each query and gathers data
	query_results = make_queries(form_dict)
	# tally the neighborhoods in query results
	nb_count = count_neighborhoods(query_results)
	return find_three_most_common(nb_count)
