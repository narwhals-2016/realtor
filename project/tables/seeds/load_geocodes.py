
#    This program updates Neighborhood table. 
import urllib
import pprint
from urllib.request import urlopen
import json
from urllib.parse import quote
import geopy
from geopy import geocoders
from geopy.geocoders import Nominatim
from geopy.geocoders import GeocoderDotUS
# Astoria latitude,longitude=40.7720145,-73.9302672 
api_key  = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
api_key2 = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
import os
import pandas as pd
from tables.models import Neighborhood



def load_geocodes():
	objects = Neighborhood.objects.all()

	geolocator = Nominatim()
	nb_lst = []
	print('total nbs: ',len(objects))
	for i in range(0, len(objects)):
		nb_lst.append(objects[i].name)
		item = objects[i].name+', NY'
		location = geolocator.geocode(item)
		# if location:
		# 	print('loc: ',location, location.latitude, location.longitude)
		# else:
		# 	print(item, 'None, None')
		update_db(objects[i].name, location)


	print('no. of nbs: ',len(nb_lst))
	list_of_cols = ['latitude', 'longitude']

def update_db(nb, location):
	temp = Neighborhood.objects.get(name=nb)
	if location:
		print('loc: ',location, location.latitude, location.longitude)
		temp.latitude = location.latitude
		temp.longitude = location.longitude
	else:
		print(nb, 'None, None')
		temp.latitude  = 'None'
		temp.longitude = 'None'
	temp.save()

def run():
	load_geocodes()
