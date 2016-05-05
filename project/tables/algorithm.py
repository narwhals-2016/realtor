from tables.models import (
	Ages, Demographic, Economic, UnitDescription, 
	SchoolEducation, Building, Score, UnitValue, 
	Neighborhood, School, StreetEasy,
)
from pprint import pprint
from numpy import repeat
# expecting that Jack's tuples 
# will match up form's input results--not the keys but the values--
# with fields in the database. if not can make a dictionary here
# with those mappings, like the tables_map


# which tables to query for given form input 
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
	'price_range': UnitValue,
	'marital_status_checkbox': Demographic,
	'number_of_vehicles': UnitDescription,
	# 'number_of_children': ??,
	# 'school_quality_importance': SchoolEducation,
	'school_level': School,
}

range_list = [
	'income_level_range',
	'price_range',
	# 'commute_time_range',
]

importance_fields_three_levels = {
	'night_life_importance': 'night_life_score',
}

importance_fields_two_levels = [
	'noise_level_checkbox',
	'crime_level_checkbox',
]


def put_value_in_group(ownership_type, key, value):
	if key == 'income_level_range':
		print('INCOME GROUP')
		if 0 <= value < 50:
			result = 'income_0_50'
		elif 50 <= value < 100:
			result = 'income_50_100'
		elif 100 <= value < 200:
			result = 'income_100_200'
		elif value >= 200:
			result = 'income_200_plus'
	elif key == 'price_range':
		# assume a renter if left ownership type left blank
		if ownership_type == 'resident_type_renter' or ownership_type == 'empty':
			print('RENT GROUP')
			if 0 <= value < 1000:
				result = 'gross_rent_1000_less'
			elif 1000 <= value < 1500:
				result = 'gross_rent_1000_1500'
			elif value >= 1500:
				result = 'gross_rent_1500_plus'
		elif ownership_type == 'resident_type_owner':
			print('PURCHASE GROUP')
			if 0 <= value < 500:
				result = 'value_of_unit_500_less'
			elif 500 <= value < 1000:
				result = 'value_of_unit_500_1M'
			elif value >= 1000:
				result = 'value_of_unit_1M_plus'
	return result



def make_queries(form):
	ten_results = {}
	for key in form:
		# perform 'ten best' query for each key in form results #
		# if the form results mapping of choices in forms.py for 
		# SearchForm works, can just use form[key] for field
		if form[key] == 'empty':
			continue
		if key in tables_map:
			print('in tables_map', key)
			if key in range_list:
				print('ownership_type', form['ownership_type'])
				field = put_value_in_group(form['ownership_type'], key, int(form[key]))
				ten_results[key] = sort_by_largest_to_smallest(table=tables_map[key], field=field)
			elif key in importance_fields_two_levels:
				ten_results[key] = sort_by_smallest_to_largest(table=tables_map[key], field=form[key])
			elif key in importance_fields_three_levels:
				if form[key] == 'high':
					ten_results[key] = sort_by_smallest_to_largest(
						table=tables_map[key], field=importance_fields_three_levels[key]
					)
				elif form[key] == 'very_high':
					# increase count for top neighborhoods in very important categories
					nb_list = sort_by_smallest_to_largest(
						table=tables_map[key], field=importance_fields_three_levels[key]
					)
					new_list = repeat(nb_list, 2)
					ten_results[key] = new_list
			else:
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
			if result.neighborhood in nb_counter:
				print(result.neighborhood)
				nb_counter[result.neighborhood] += 1
			else:
				# if not in nb_counter, add to nb_counter
				nb_counter[result.neighborhood] = 1
	# sorts least to greatest, returns array of tuples of neighborhood and count
	return nb_counter



def get_nb_data(nb_list, count, school_level):
	pics =[
		"http://img.theepochtimes.com/n3/eet-content/uploads/2014/09/12/shutterstock_201591710-676x450.jpg",
		"http://fc3d750e1b22019028ae-eb9d0534c31fede444754f378d638c42.r70.cf1.rackcdn.com/uploads/picture/source/1184/victorian_homes_BH.jpg",
		"http://images.nymag.com/realestate/neighborhoods/2010/nabelivable100419_opener_560.jpg",
		"http://farm5.static.flickr.com/4035/5134152910_2f64668299.jpg",
		"http://www.arizonafoothillsmagazine.com/valleygirlblog/wp-content/uploads/9-tie-new-york-ny-10065-nycs-upper-east-side-neighborhood-from-60th-street-to-69th-street-had-six-home-sales-over-10-million.jpg",
		"http://www.asliceofbrooklyn.com/wp-content/uploads/2015/02/street-view-brooklyn-slider.jpg",
		"http://www.nychomes4u.com/wp-content/uploads/photo-gallery/brooklyn%204.png",
		"http://www.arizonafoothillsmagazine.com/valleygirlblog/wp-content/uploads/9-tie-new-york-ny-10065-nycs-upper-east-side-neighborhood-from-60th-street-to-69th-street-had-six-home-sales-over-10-million.jpg",
		"http://www.asliceofbrooklyn.com/wp-content/uploads/2015/02/street-view-brooklyn-slider.jpg",
		"http://hometown-tourist.com/wp-content/uploads/2015/01/Manhattan-Neighborhood-Street-Scene.jpg",
		"http://www.nychomes4u.com/wp-content/uploads/photo-gallery/brooklyn%204.png",
		"http://fc3d750e1b22019028ae-eb9d0534c31fede444754f378d638c42.r70.cf1.rackcdn.com/uploads/picture/source/1184/victorian_homes_BH.jpg",
	]

	# get age_median, income_median, rent_median
	data = []
	for nb in nb_list:
		print(nb.webdisplay)
		nb_dict = {}
		nb_dict['webdisplay'] = nb.webdisplay + ", " + nb.borough
		nb_dict['age_median'] = str(Ages.objects.get(neighborhood=nb).age_median)
		nb_dict['income_median'] = str(Economic.objects.get(neighborhood=nb).median_income)
		nb_dict['rent_median'] = str(UnitValue.objects.get(neighborhood=nb).gross_rent_median)
		nb_dict['rooms_median'] = str(UnitDescription.objects.get(neighborhood=nb).rooms_median)
		nb_dict['commute_score'] = str(Score.objects.get(neighborhood=nb).commute_score)
		nb_dict['pic_link'] = nb.pic_link
		nb_dict["link"] = pics[count]
		nb_dict['latitude'] = nb.latitude
		nb_dict['longitude'] = nb.longitude
		nb_dict['sqft_median'] = str(StreetEasy.objects.get(neighborhood=nb).squarefeet_median)
		if nb_dict['sqft_median'] == '0.00':
			print('sqft equals 0.00')
			nb_dict['sqft_median'] = 'Information not Available'
		print(nb_dict['sqft_median'])
		school_score = getattr(School.objects.get(neighborhood=nb), school_level, None)		
		if school_score:
			nb_dict['school_score'] = str(school_score)
		
		count +=1 
		data.append(nb_dict)
	return data

def find_n_most_common(nb_dict, n):
	sorted_dict = sorted(nb_dict.items(), key = lambda x:x[1], reverse=True)
	# gets the last n, or the ones with the highest count
	n_most_common = sorted_dict[:n]
	return [n_most_common, sorted_dict]

def filter_commute(nb_list, sorted_neighborhoods, commute_cap):
	print('IN FILTERED COMMUTE')
	print('CAP', commute_cap)
	nb_list_length = len(nb_list)
	for nb in nb_list:
		if Score.objects.get(neighborhood=nb).commute_score > commute_cap:
			print('removing bc commute', nb)
			nb_list.remove(nb)
			nb_list.append(sorted_neighborhoods.pop(nb_list_length)[0])
	return nb_list

def filter_school(nb_list, sorted_neighborhoods, school_quality, school_level):
	print('IN FILTERED SCHOOL')
	print('IMPORTANCE CHOICE', school_quality)
	print(school_level)
	nb_list_length = len(nb_list)
	if school_quality == 'high':
		for nb in nb_list:
			school_obj = School.objects.get(neighborhood=nb)
			level = getattr(school_obj, school_level, 10)
			if level < 3:
				print('removing bc school', nb)
				nb_list.remove(nb)
				nb_list.append(sorted_neighborhoods.pop(nb_list_length)[0])
	elif school_quality == 'very_high':
		for nb in nb_list:
			school_obj = School.objects.get(neighborhood=nb)
			level = getattr(school_obj, school_level, 10)
			if level < 4:
				print('removing bc school', nb)
				nb_list.remove(nb)
				nb_list.append(sorted_neighborhoods.pop(nb_list_length)[0])
	return nb_list


def filter_price(nb_list, sorted_neighborhoods, price_cap, ownership_type):
	print('IN FILTERED PRICE')
	print('CAP', price_cap + 200)
	print(ownership_type)
	nb_list_length = len(nb_list)
	for nb in nb_list:
		uv_obj = UnitValue.objects.get(neighborhood=nb)
		if ownership_type == 'resident_type_renter':		
			if UnitValue.objects.get(neighborhood=nb).gross_rent_median > price_cap + 200:
				print('removing bc price', nb)
				nb_list.remove(nb)
				nb_list.append(sorted_neighborhoods.pop(nb_list_length)[0])
		elif ownership_type == 'resident_type_owner':
			if UnitValue.objects.get(neighborhood=nb).value_of_unit_median > price_cap + 200:
				print('removing bc price', nb)
				nb_list.remove(nb)
				nb_list.append(sorted_neighborhoods.pop(nb_list_length)[0])
	return nb_list


def get_results(form_dict):
	commute_cap = int(form_dict.get('commute_time_range', '1000'))
	price_cap = int(form_dict.get('price_range', '20000'))
	ownership_type = form_dict.get('ownership_type', 'empty')
	school_quality = form_dict.get('school_quality_importance', 'empty')
	school_level = form_dict.get('school_level', 'empty')
	# performs each query and gathers data
	query_results = make_queries(form_dict)
	# tally the neighborhoods in query results
	nb_count = count_neighborhoods(query_results)
	n_most_common, sorted_dict = find_n_most_common(nb_count, 9)
	n_most_common = [nb[0] for nb in n_most_common]

	n_most_common = filter_commute(n_most_common, sorted_dict, commute_cap)
	n_most_common = filter_price(n_most_common, sorted_dict, price_cap, ownership_type)
	n_most_common = filter_school(n_most_common, sorted_dict, school_quality, school_level)
	return (n_most_common, school_level)

