from tables.models import Neighborhood, StreetEasy
from tables.streeteasy import combo_map
from tables.seeds.mappings.mappings import nb_zip

# result from api comes as dictionary of zip_code:{api output}
# use combo_map for api_mapping parameter

# use nb_zip as zip_mapping parameter
# input nb:[zips] mapping as zip_mapping

# def get_neighborhood(nb):
	# nb_filter = Neighborhood.objects.filter(name=nb)
	# return nb_filter

def make_streeteasy_score(nb_obj, zip_list):
	rent_median = sum([int(zip_code['median_price']) for zip_code in zip_list])/len(zip_list)
	rent_average = sum([int(zip_code['average_price']) for zip_code in zip_list])/len(zip_list)
	squarefeet_median = sum([int(zip_code['median_sqft']) for zip_code in zip_list])/len(zip_list)
	squarefeet_average = sum([int(zip_code['average_sqft']) for zip_code in zip_list])/len(zip_list)
	
	street_tuple = StreetEasy.objects.get_or_create(
		neighborhood= nb_obj,
		defaults={
			'neighborhood': nb_obj,
			'rent_median': rent_median,
			'rent_average': rent_average,
			'squarefeet_median': squarefeet_median,
			'squarefeet_average': squarefeet_average,

		}
	)
	print(street_tuple)
	return street_tuple

def get_zip_code_scores(zip_list, api_mapping):
	print("inside get_zip_code_scores", zip_list)
	result_holder = []
	for zip_code in zip_list:
		api_dict = api_mapping.get(zip_code, 'empty')
		print(api_dict)
		if api_dict == 'empty':
			print('EMPTY', zip_code)
			continue
		else:
			result_holder.append(api_dict)

	return result_holder


def run(zip_mapping, api_mapping):
	for nb in zip_mapping:
		nb_filter = Neighborhood.objects.filter(name=nb)
		if nb_filter:
			print("got nb_obj", nb)
			nb_obj = nb_filter[0]
			zip_list = zip_mapping[nb_obj.name]
			zip_score_list = get_zip_code_scores(zip_list, api_mapping)
			make_streeteasy_score(nb_obj, zip_score_list)
		else:
			print("didn't get nb_obj", nb)



