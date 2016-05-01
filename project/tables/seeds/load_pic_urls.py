import urllib
import pprint
from urllib.request import urlopen
import json
from urllib.parse import quote
api_key  = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
api_key2 = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
import os
import pandas as pd
from tables.models import Neighborhood


def url_for_place_id(nb_search, typ):
	url_base = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
	key_string = '?key='+ api_key
	location_string   = '&location='+nb_search
	sensor_string = '&sensor=false'
	radius_string = '&radius=500'
	type_string = '&type='+typ
	url = url_base+key_string+location_string+sensor_string+type_string+radius_string
	return url

def urls_for_photos(photo_id):
	url_base      = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='
	photoref_string = photo_id
	key_string    = '&key='+ api_key2
	url = url_base+photoref_string+key_string
	return url

def create_pic_url(nb_search):
	
	type_list = ['restaurant','cafe','night_club','park']
	for typ in type_list:
		url_str = url_for_place_id(nb_search, typ)
		rawData = urllib.request.urlopen(url_str).read().decode('UTF-8')
		jsonData = json.loads(rawData)
		searchResults = jsonData["results"]
		photo_url_list = []
		photo_ref_list = []
		for i in searchResults:
			pp = pprint.PrettyPrinter(indent=4)
			for key, val in i.items():
				if key == 'photos':
					lst = val
					photo_ref_list.append(lst[0]['photo_reference'])	
					for ref in photo_ref_list:
						photo_url_list.append(urls_for_photos(ref))
	return photo_url_list

def update_db(nb, pic_url):
	#print(nb, 'in update db: *****************************************')
	#print('URLLL: ',pic_url)
	temp = Neighborhood.objects.get(name=nb)
	print('no of urls: ', len(pic_url))
	if len(pic_url)>0:
		temp.pic_link = pic_url[0]
	temp.save()

def	load_pic_urls():

	objects = Neighborhood.objects.all()

	nb_lst = []
	for i in range(0, len(objects)):
		nb_lst.append(objects[i].name)
		if objects[i].latitude != 'None':
			
			nb_search=(str(objects[i].latitude)+','+str(objects[i].longitude)).replace(" ","")

			picture_url = create_pic_url(nb_search)
			print('picture list: ', len(picture_url))
			update_db(objects[i].name, picture_url)


def run():
	
	load_pic_urls()
