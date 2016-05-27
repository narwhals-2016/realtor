"""
1 . put all tables into dataframe
>>> import tables.dataframe as d
>>> l = prefetch_related()
>>> df = from_records(l)
simulat
"""
from tables.models import (
	Ages, Demographic, Economic, UnitDescription, 
	SchoolEducation, Building, Score, UnitValue, 
	Neighborhood, School, StreetEasy,
)
from django.db.models import Q
from pprint import pprint
import pandas as pd 
from sklearn.metrics.pairwise import euclidean_distances

# prefetch should cut down subsequent queries; all the data for each neighborhood collected at once
# beware space issue
def prefetch_related():
	return Neighborhood.objects.prefetch_related(
		'ages_set','demographic_set', 'economic_set', 'unitdescription_set',
		'schooleducation_set', 'building_set', 'score_set', 'unitvalue_set',
		'school_set', 'streeteasy_set',
		).all().values(
			# "id", 
			"name", 
			# "webdisplay",
			# "borough", 
			# "latitude", 
			# "longitude", 
			"ages__age_0_19", "ages__age_20_24", "ages__age_25_34", "ages__age_35_64", "ages__age_65_over", "ages__age_median", 
			"building__number_of_units_2_less", "building__number_of_units_3_10", "building__number_of_units_10_plus", "building__constucted_before_1970", "building__constucted_1970_2000", "building__constucted_after_2000",
			"demographic__married", "demographic__divorced", "demographic__one_yr_turnover", "demographic__birth_native", "demographic__birth_foreign", "demographic__gender_m", "demographic__gender_f", 
			"economic__laborforce", "economic__unemployed", "economic__below_poverty_level", "economic__income_0_50", "economic__income_50_100", "economic__income_100_200", "economic__income_200_plus", "economic__median_income", "economic__mean_income",
			"school__k_school_score", "school__elem_school_score", "school__hs_school_score",
			"schooleducation__school_enrollment_pre_highschool", "schooleducation__school_enrollment_highschool", "schooleducation__school_enrollment_college", "schooleducation__education_highschool_over", "schooleducation__education_college_over", 
			"score__night_life_score", "score__commute_score", "score__crime_score", "score__noise_score", 
			"streeteasy__rent_median", "streeteasy__rent_average", "streeteasy__squarefeet_median", "streeteasy__squarefeet_average", 
			"unitdescription__units_occupied", "unitdescription__units_vacant", "unitdescription__rooms_per_unit_1", "unitdescription__rooms_per_unit_2", "unitdescription__rooms_per_unit_3_5", "unitdescription__rooms_per_unit_6_plus", "unitdescription__rooms_median", "unitdescription__resident_type_owner", "unitdescription__resident_type_renter", "unitdescription__length_residence_before_2000", "unitdescription__length_residence_2000_2009", "unitdescription__length_residence_after_2010", "unitdescription__vehicles_0", "unitdescription__vehicles_1_plus",
			"unitvalue__value_of_unit_500_less", "unitvalue__value_of_unit_500_1M", "unitvalue__value_of_unit_1M_plus", "unitvalue__value_of_unit_median", "unitvalue__gross_rent_1000_less", "unitvalue__gross_rent_1000_1500", "unitvalue__gross_rent_1500_plus", "unitvalue__gross_rent_median",
		)


def from_records(dict_list):
	return pd.DataFrame.from_records(dict_list)

# df = from_records(prefetch_related()).set_index(['name'])


"""
euclidean_distances(df, query) will return an array with the distances of every df row to the query
"""
def add_euclidean_distance(df, query):
	df['euclidean_distance'] = euclidean_distances(df, query)
	return df

def sort_df_by_euclidean_distance(df):
	return df.sort_values('euclidean_distance')


"""
CD {'noise_level_checkbox': 'on', 'night_life_importance': 'high', 'current_edu_level': 'hs', 'school_quality_importance': 'high', 'age': '20_24', 
'price_range': '1125', 'gender': 'male', 'number_of_children': '1_plus', 'income_level_range': '135', 'ownership_type': 'purchase', 'number_of_units': '3_10', 
'commute_time_range': '53', 'building_age': 'post_1970', 'school_level': 'school_1-8', 'crime_level_checkbox': 'on'}



field_mappings {'noise_level_checkbox': 'noise_score', 'highest_edu_level': 'empty', 'commute_address': 'empty', 'boroughs': 'empty', 
'current_edu_level': 'school_enrollment_highschool', 'income_level_range': '135', 'gender': 'gender_m', 'commute_type': 'empty', 'commute_time_range': '53', 
'number_of_rooms': 'empty', 'price_range': '1125', 'number_of_vehicles_checkbox': 'empty', 'night_life_importance': 'high', 'school_quality_importance': 'high', 
'age': 'age_20_24', 'ownership_type': 'resident_type_owner', 'number_of_children': '1_2', 'number_of_units': 'number_of_units_3_10', 'marital_status_checkbox': 'empty', 
'building_age': 'constucted_1970_2000', 'school_level': 'elem_school_score', 'crime_level_checkbox': 'crime_score'}
"""
# example form input mapped to proper fields
field_mappings = {
	'noise_level_checkbox': 'noise_score', 'highest_edu_level': 'empty', 'commute_address': 'empty', 
	'boroughs': 'empty', 'current_edu_level': 'school_enrollment_highschool', 
	'income_level_range': '135', 'gender': 'gender_m', 'commute_type': 'empty', 'commute_time_range': '53', 
	'number_of_rooms': 'empty', 'price_range': '1125', 'number_of_vehicles_checkbox': 'empty', 
	'night_life_importance': 'high', 'school_quality_importance': 'high', 
	'age': 'age_20_24', 'ownership_type': 'resident_type_owner', 'number_of_children': '1_2', 
	'number_of_units': 'number_of_units_3_10', 'marital_status_checkbox': 'empty', 
	'building_age': 'constucted_1970_2000', 'school_level': 'elem_school_score', 
	'crime_level_checkbox': 'crime_score'
}

table_prefix_map = {
    'age': 'ages',
    'gender': 'demographic',
    'current_edu_level': 'schooleducation', 
    'highest_edu_level': 'schooleducation', 
    'number_of_units': 'building', 
    'building_age': 'building', 
    'ownership_type': 'unitdescription',
    'number_of_rooms': 'unitdescription',
    'commute_time_range': 'score',
    'night_life_importance': 'score', 
    'noise_level_checkbox': 'score', 
    'crime_level_checkbox': 'score', 
    'income_level_range': 'economic',
    # 'price_range': 'unitvalue',
    'marital_status_checkbox': 'demographic',
    'number_of_vehicles': 'unitdescription',
    # 'number_of_children': ??,
    # 'school_quality_importance': SchoolEducation,
    'school_level': 'school',
}

one_to_one_map = {
	'night_life_importance': 'score__night_life_score',
	'income_level_range': 'economic__median_income',
	'commute_time_range': 'score__commute_score',
}

# what type of score to generate for query df row
# uses form keys, not the 
type_dict = {
	'proportional':[
		'age', 'gender', 'current_edu_level', 'highest_edu_level', 'number_of_units',
		'building_age', 'ownership_type', 'number_of_rooms', 'number_of_vehicles',
		'marital_status_checkbox',
	],
	'value':['income_level_range', 'price_range', 'commute_time_range'],
	'high_score':['night_life_importance', 'school_level'],
	'low_score':['noise_level_checkbox', 'crime_level_checkbox'],
}

# field mappings is what's passed
def get_values(form):
	series = pd.Series()
	value_list = []
	value_list.append('name')
	for key in form:
		if form[key] == 'empty':
			continue
		if key in table_prefix_map:
			print(key)
			if key in one_to_one_map:
				value = one_to_one_map[key]
				value_list.append(value)
				if key == 'night_life_importance':
					series[value] = 3
				else:
					series[value] = form[key]
			else:
				# outputs the table and the field
				value = table_prefix_map[key] + '__' + form[key]
				col_val = make_series_col(key)
				series[value] = col_val	
				value_list.append(value)
	return (value_list, series)

def make_series_col(form_key):
	for key in type_dict:
		if form_key in type_dict[key]:
			if key == 'proportional':
				return 100
			elif key == 'low_score':
				return 0
			elif key == 'high_score':
				if form_key == 'school_level':
					return 5
				elif form_key == 'night_life_importance':
					return 10

def prefetch(value_list):
	return Neighborhood.objects.prefetch_related(
		'ages_set','demographic_set', 'economic_set', 'unitdescription_set',
		'schooleducation_set', 'building_set', 'score_set', 'unitvalue_set',
		'school_set', 'streeteasy_set',
		).all().values(*value_list)

v = get_values(field_mappings)
p = prefetch(v[0])




















