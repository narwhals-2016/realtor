"""
Add census neighborhoods to django models Neighborhood
python commands to run in 'python3 manage.py shell' 
>>> from tables.load_neighborhoods import run
>>> run()
"""

import os
import pandas as pd
from tables.models import Neighborhood
from tables.seeds.mappings.mappings import name_mappings, borough_mappings

def parse_file(filename):
	# use pandas to read excel file, and then create dataframe with first column as index
	housing_file = pd.read_excel(filename, skiprows=[2,3], sheetname=0)

	indexed = housing_file.set_index('2009-2013 ACS Housing Profile')
	return indexed

def get_neighborhood_name(dataframe):
	# neighborhood given in first row of indexes, must be parsed out
	neighborhood_string = dataframe.index[0]
	return neighborhood_string[23:]

def	load_neighborhood(neighborhood):
	print('in load_neighborhood', neighborhood)
	nb, created = Neighborhood.objects.get_or_create(
		name=neighborhood,
		defaults={
			'name': neighborhood,
			# default webdisplay name is census neighborhood name:
			'webdisplay': neighborhood,
		}
	)
	print('object check', type(nb))
	if created == False:
		print('object name before update', nb.name)
		print('neighborhood string name', neighborhood)
		nb.name = neighborhood
		nb.webdisplay = neighborhood
		nb.save()
		print('********UPDATED', nb.name)
	else:
		print('nb_obj created********', nb.name)
	return True


def run(folder_path, folder):
	file_list = os.listdir(folder_path + folder)
	for filename in file_list:
		dataframe = parse_file(folder_path + folder + '/' + filename)
		neighborhood = get_neighborhood_name(dataframe)
		if neighborhood != "Rikers Island":
			load_neighborhood(neighborhood)
		else:
			print('RIKERS -- PASS ****************')
			continue

	load_display_names(name_mappings)
	load_boroughs(borough_mappings)
	print('LOAD_NEIGHBORHOOD DONE')
	return True


# run only after neighborhoods loaded
# name_mappings = {nb: name}
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

# borough_mappings = {nb: borough}
def load_boroughs(borough_mappings):
	neighborhoods = Neighborhood.objects.all()
	for neighborhood in borough_mappings:
		nb_filter = Neighborhood.objects.filter(name=neighborhood)
		if nb_filter:
			print('old display_name', nb_filter[0].borough)
			nb_filter[0].borough = borough_mappings[neighborhood]
			nb_filter[0].save()
			print('new display_name', nb_filter[0].borough)
	return True

