"""
Add census neighborhoods to django models Neighborhood
python commands to run in 'python3 manage.py shell' 
>>> from tables.load_neighborhoods import run
>>> run()
"""

import os
import pandas as pd
from tables.models import Neighborhood
from tables.seeds.mappings.mappings import name_mappings

def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3], sheetname=0)

	indexed = housing_file.set_index('2009-2013 ACS Housing Profile')
	return load_neighborhood(indexed)

def	load_neighborhood(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	neighborhood = neighborhood_string[23:]
	print('in load_neighborhood', neighborhood)

	neighborhood_tuple = Neighborhood.objects.get_or_create(
		name=neighborhood,
		defaults={
			'name': neighborhood,
			# default webdisplay name is census neighborhood name:
			'webdisplay': neighborhood,
		}
	)
	
	if neighborhood_tuple[1] == False:
		neighborhood_tuple[0].name = neighborhood,
		neighborhood_tuple[0].webdisplay = neighborhood,
		neighborhood_tuple[0].save()
		print('********UPDATED', neighborhood_tuple[0].name)
	else:
		print('nb_obj created********', neighborhood_tuple[0].name)
	# options if neighborhood already in table:


def run(folder_path, folder):
	file_list = os.listdir(folder_path + folder)
	for filename in file_list:
		parse_file(folder_path + folder + '/' + filename)
	load_display_names(name_mappings)
	print('LOAD_NEIGHBORHOOD DONE')
	return True


# run only after neighborhoods loaded
def load_display_names(name_mappings):
	neighborhoods = Neighborhood.objects.all()
	for neighborhood in name_mappings:
		nb_filter = Neighborhood.objects.filter(name=neighborhood)
		if nb_filter:
			print('old display_name', nb_filter[0].webdisplay)
			nb_filter[0].webdisplay = name_mappings[neighborhood]
			nb_filter[0].save()
			print('new display_name', nb_filter[0].webdisplay)
	return True
