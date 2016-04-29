
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
import os
import pandas as pd
from tables.models import Neighborhood



def load_geocodes():
	objects = Neighborhood.objects.all()

	geolocator = Nominatim()
	nb_lst = []

	for i in range(0, len(objects)):
		nb_lst.append(objects[i].name)
		item = objects[i].name+', NY'
		location = geolocator.geocode(item)
		update_db(objects[i].name, location)

def update_db(nb, location):
	
	temp = Neighborhood.objects.get(name=nb)
	if location:
		temp.latitude = location.latitude
		temp.longitude = location.longitude
	else:
		temp.latitude  = 'None'
		temp.longitude = 'None'
	temp.save()

def run():
	load_geocodes()
