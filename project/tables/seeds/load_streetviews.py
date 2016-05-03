#https://maps.googleapis.com/maps/api/streetview?size=600x300&location=46.414382,10.013988&heading=151.78&pitch=-0.76&key

#    This program updates Neighborhood table. 
import urllib
import pprint
from urllib.request import urlopen
import json
from urllib.parse import quote
# Astoria latitude,longitude=40.7720145,-73.9302672 
api_key  = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
api_key2 = 'AIzaSyBh35VVKt0RiXEbZlpLwglvt3rXau9kyvA'
#street_api_key='AIzaSyBAgoB32NskmQcPOACy0DlFhhy0WERTskI'
street_api_key='AIzaSyBAgoB32NskmQcPOACy0DlFhhy0WERTskI'
import os
import pandas as pd
from tables.models import Neighborhood


def urls_for_streetview(geo_corordinates):
    url_base = 'https://maps.googleapis.com/maps/api/streetview?size=600x300'
    loaction_string='&location='+geo_corordinates    
    heading_and_pitch_str='&heading=151.78&pitch=-0.76'
    key_string = '&key='+ street_api_key

    url = url_base+loaction_string+heading_and_pitch_str+key_string
    return url

# def urls_for_streetview(geo_corordinates):
#   url_base      = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference='
#   photoref_string = photo_id
#   key_string    = '&key='+ api_key2
#   url = url_base+photoref_string+key_string


def update_db():
    items = Neighborhood.objects.all()

    for i in range(0, len(items)):    
        temp = Neighborhood.objects.get(name=items[i].name)

        if items[i].latitude  != 'None':
            geostr = str(items[i].latitude+','+items[i].longitude).replace(" ","")
            street_url = urls_for_streetview(geostr)
            temp.pic_link  = street_url
            temp.save()
            print('streetview saved', items[i].name)
        else:
            print('without lat and long: ',items[i].name)

def run():
    # geos ='40.7720145,-73.9302672'
    update_db()
    #geos='46.414382,10.013988'
    # street_url = urls_for_streetview(geos)
    # print('street view: ', street_url)
