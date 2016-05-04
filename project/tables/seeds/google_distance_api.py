import requests
import json
from tables.models import Neighborhood, Score
from tables.seeds.mappings.mappings import nb_zip
from django.conf import settings 

# old dictionary don't use. Import nb_zip from mappings/mappings.py
# best_matches ={'Breezy Point-Belle Harbor-Rockaway Park-Broad': ['11697'], 'East New York': ['11207'], 'Bushwick North': ['11237'], 'Elmhurst': ['11373'], 'South Ozone Park': ['11436'], 'Arden Heights': ['MISSING'], 'Central Harlem North-Polo Grounds': ['10039'], 'Westchester-Unionport': ['10461'], 'Rosedale': ['11422'], 'Schuylerville-Throgs Neck-Edgewater Park': ['10465'], 'New Brighton-Silver Lake': ['10301'], 'Crotona Park East': ['10460'], 'Prospect Heights': ['11238'], 'Morningside Heights': ['10027'], 'Bushwick South': ['11237'], 'Port Richmond': ['10302'],  "Mariner's Harbor-Arlington-Port Ivory-Granite": ['10303'], 'Kew Gardens': ['11415'], 'Great Kills': ['10308'], 'East Elmhurst': ['11369'], 'Melrose South-Mott Haven North': ['10451'], 'Central Harlem South': ['10026'], 'Corona': ['11368'], 'West Village': ['10014', '10012'], 'Douglas Manor-Douglaston-Little Neck': ['11362'], 'Dyker Heights': ['11228'], 'Astoria': ['11103'], 'Belmont': ['10458'], 'East Harlem North': ['10037'], 'Spuyten Duyvil-Kingsbridge': ['10463'], 'Longwood': ['10455'], 'Bensonhurst West': ['11214'], 'North Side-South Side': ['MISSING'], 'Sunset Park West': ['11220'], 'Battery Park City-Lower Manhattan': ['10280', '10038', '10004', '10006', '10005'],   "Annadale-Huguenot-Prince's Bay-Eltingville": ['10312'], 'Fort Greene': ['11205'], 'Jackson Heights': ['11372'], 'Sunset Park East': ['11220'], 'Auburndale': ['11358'], 'West Farms-Bronx River': ['10460'], 'Greenpoint': ['11222'], 'New Dorp-Midland Beach': ['10306'], 'Oakland Gardens': ['11364'], 'College Point': ['11356'], 'Hunters Point-Sunnyside-West Maspeth': ['11104'], 'Jamaica': ['11432'], 'Chinatown': ['10013'], 'Flatbush': ['11226'], 'Madison': ['11229'], 'Allerton-Pelham Gardens': ['10312'], 'Bay Ridge': ['11209'], 'Queensboro Hill': ['11355'], 'Ocean Hill': ['11233'], 'Clinton': ['10036', '10019', '10018'], 'Brighton Beach': ['11235'], 'Eastchester-Edenwald-Baychester': ['10475'], 'Williamsbridge-Olinville': ['10467', '11249'], 'Woodside': ['11377'], 'Bath Beach': ['11214'], 'Briarwood-Jamaica Hills': ['11435'], 'Kensington-Ocean Parkway': ['11218'], 'West Concourse': ['10451'], 'Van Cortlandt Village': ['10468'], 'Stapleton-Rosebank': ['10305'], 'North Riverdale-Fieldston-Riverdale': ['10471'], 'Ridgewood': ['11385'], 'Cypress Hills-City Line': ['11208'], 'Gramercy': ['10003'], 'Ft. Totten-Bay Terrace-Clearview': ['11360'], 'Pelham Parkway': ['10062'], 'Maspeth': ['11378'], 'Hamilton Heights': ['10031'], 'Homecrest': ['11223'], 'Mott Haven-Port Morris': ['10454'], 'Richmond Hill': ['11418'], 'Queens Village': ['11428'], 'Canarsie': ['11236'], 'Cambria Heights': ['11411'], 'Bensonhurst East': ['11204'], 'Rossville-Woodrow': ['10309'], 'East Harlem South': ['10029'], 'Far Rockaway-Bayswater': ['11691'], 'Charleston-Richmond Valley-Tottenville': ['10307'], 'Lenox Hill-Roosevelt Island': ['10065'], 'Fresh Meadows-Utopia': ['11365'], 'Forest Hills': ['11375'], 'Lower East Side': ['10002'], 'West Brighton': ['10310'], 'Lindenwood-Howard Beach': ['11414'], 'Carroll Gardens-Columbia Street-Red Hook': ['11231'], 'Ozone Park': ['11417'], 'Bronxdale': ['10462'], 'Crown Heights South': ['11225'], 'Co-Op City': ['10475'], 'Bedford': ['11216'], 'Glen Oaks-Floral Park-New Hyde Park': ['11040'], 'Baisley Park': ['11434'], 'Queensbridge-Ravenswood-Long Island City': ['11106', '11101'], 'Kew Gardens Hills': ['11415'], 'Seagate-Coney Island': ['11224'], 'Pomonok-Flushing Heights-Hillcrest': ['11354', '11206'], 'Bedford Park-Fordham North': ['10458'], 'Van Nest-Morris Park-Westchester Square': ['10462'], 'Flushing': ['11354'], 'Oakwood-Oakwood Beach': ['10306'], 'Soundview-Bruckner': ['10472'], 'Stuyvesant Heights': ['11233'], 'Washington Heights South': ['10033'], 'Glendale': ['11385'], 'University Heights-Morris Heights': ['10453'], 'Old Astoria': ['11102'], 'Todt Hill-Emerson Hill-Heartland Village-Ligh': ['10304'], 'St. Albans': ['11412'], 'Parkchester': ['10462'], 'Washington Heights North': ['10040', '10032', '10033'], 'Elmhurst-Maspeth': ['11373'], 'Hudson Yards-Chelsea-Flat Iron-Union Square': ['10011', '10001'], 'Marble Hill-Inwood': ['10034'], 'Woodhaven': ['11421'], 'Stuyvesant Town-Cooper Village': ['10009', '10010'], 'Springfield Gardens North': ['11413'], 'Rego Park': ['11374'], 'New Springville-Bloomfield-Travis': ['10314'], 'Hollis': ['11423'], 'Springfield Gardens South-Brookville': ['11413'], 'Brooklyn Heights-Cobble Hill': ['11201'], 'Turtle Bay-East Midtown': ['10022'], 'Manhattanville': ['10027'], 'Lincoln Square': ['10023'], 'Murray Hill': ['10016'], 'Flatlands': ['11234'], 'East Concourse-Concourse Village': ['10451'], 'DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H': ['11201', '11217'], 'Pelham Bay-Country Club-City Island': ['10464'], 'North Corona': ['11368'], 'Gravesend': ['11223'], 'Morrisania-Melrose': ['10456'], 'Old Town-Dongan Hills-South Beach': ['10305'], 'Bellerose': ['11426'], 'Mount Hope': ['10003'], 'East New York (Pennsylvania Ave)': ['11207'], 'South Jamaica': ['11433'], 'Brownsville': ['11212'], 'Grymes Hill-Clifton-Fox Hills': ['10301'], 'Windsor Terrace': ['11215'], 'Borough Park': ['11219'], 'Erasmus': ['11226'], 'Kingsbridge Heights': ['10463'], 'Highbridge': ['10452'], 'Midwood': ['11230'], 'Woodlawn-Wakefield': ['10466'], 'Whitestone': ['11357'], 'West New Brighton-New Brighton-St. George': ['10310'], 'Middle Village': ['11379'], 'East Flushing': ['11354'], 'Hunts Point': ['10474'], 'Crown Heights North': ['11225'], 'Hammels-Arverne-Edgemere': ['11692'], 'SoHo-TriBeCa-Civic Center-Little Italy': ['10013', '10007'], 'Midtown-Midtown South': ['10019'], 'Sheepshead Bay-Gerritsen Beach-Manhattan Beac': ['11235'], 'Soundview-Castle Hill-Clason Point-Harding Pa': ['10472'], 'East Tremont': ['10457'], 'Laurelton': ['11413'], 'Murray Hill-Kips Bay': ['10016'], 'Rikers Island': ['MISSING'], 'Starrett City': ['11239'], 'Bayside-Bayside Hills': ['11361'], 'Ocean Parkway South': ['11230'], 'Norwood': ['10467'], 'Claremont-Bathgate': ['10457'], 'Rugby-Remsen Village': ['11203'], 'Prospect Lefferts Gardens-Wingate': ['11225'], 'Jamaica Estates-Holliswood': ['11423'], 'Fordham South': ['10458'], 'East Williamsburg': ['11211'], 'Clinton Hill': ['11205'], 'Yorkville': ['10128'], 'Upper West Side': ['10024', '10025'], 'Steinway': ['11105'], 'East Village': ['10009'], 'Georgetown-Marine Park-Bergen Beach-Mill Basi': ['11234'], 'East Flatbush-Farragut': ['11203'], 'Grasmere-Arrochar-Ft. Wadsworth': ['10304'], 'Westerleigh': ['10314'], 'Williamsburg': ['11211'], 'Upper East Side-Carnegie Hill': ['10128', '10028', '10075', '10021']}
destinations = ["time+square+NYC|","union+square+NY|", "chamber+street+NY|", "59th+st+NY"]

params = {
   'destinations':destinations[0]+destinations[1]+destinations[2]+destinations[3],
   'mode':"transit",
   'units':"imperial",
   'traffic_model':"pessimistic",
   'transit_mode':"rail",
}

class GoogleAPI:

    def __init__(self, access_token):
     self.access_token = access_token

    def get(self,path,**kwargs):
     # this builds the begining of the URL 
     URL = "https://maps.googleapis.com/maps/api/" + path
     # this adds all the attributes to the end of the URL
     params = kwargs.get("params")
     # this adds the acces token to be passed to the api
     params.update({"key":self.access_token})
     return requests.get(URL,params=params) 

# create an instance of the api
api = GoogleAPI(settings.GOOGLE_KEY)


def get_commute_stats(params, destinations,nb_zip, api):
    missing=0
    missing_array =[]
    # this creates a dict with a list of all the neighborhoods
    neighborhood_commute_dict = dict.fromkeys(nb_zip)

    # calls the api with the params for every origin 
    for i in neighborhood_commute_dict: 
        origin = str(i)+"+NY"
        print (origin)
        params['origins']=origin 

        info = api.get('distancematrix/json', params=params)
        response_info = info.json()
        # print (response_info)

        try:
            time_sq_score = response_info["rows"][0]["elements"][0]["duration"]["value"]
            union_sq_score = response_info["rows"][0]["elements"][1]["duration"]["value"]
            chamber_st_score = response_info["rows"][0]["elements"][2]["duration"]["value"]
            fifty_ninth_st_score = response_info["rows"][0]["elements"][3]["duration"]["value"]

            # this is the avg time it takes to get from the origin to the 4 major destinations, rounded to 4 places
            total_score_seconds = ((time_sq_score+union_sq_score+chamber_st_score+fifty_ninth_st_score)/4)
            total_score_min = round((total_score_seconds/60),3)

        except: 
            total_score_min = 0 #this happens for 3 places, couldnt find them using conventional searches
            missing += 1
            missing_array.append(origin)
            print ("MISSING")

        neighborhood_commute_dict[i] = total_score_min
        print(total_score_min)

    # hard code the errors 
    neighborhood_commute_dict["Bedford"] = 48.00
    neighborhood_commute_dict["Norwood"] = 0
    neighborhood_commute_dict["Mount Hope"] = 40.00
    neighborhood_commute_dict["Madison"] = 50.00
    neighborhood_commute_dict["Rugby-Remsen Village"] = 0
    neighborhood_commute_dict["Yorkville"] = 22.00
    neighborhood_commute_dict["Clinton"] = 18.00
    neighborhood_commute_dict["Stuyvesant Heights"] = 45.00

    print ("\n Done calculating minutes")
    print ("neighborhood_commute_dict = ", neighborhood_commute_dict)
    print ("missing: ", missing)
    print ("missing neighborhoods: ", missing_array)
    return neighborhood_commute_dict

def update_commute_score(commute_dict):
    # check if neighborhood exists in noise dict
    for neighborhood in commute_dict:
        # may not be able to filter on foreign key attribute
        nb_obj = Neighborhood.objects.filter(name=neighborhood)

        if nb_obj:
            nb_obj = nb_obj[0]
            # get all the scores for that nb
            score_list = Score.objects.filter(neighborhood=nb_obj)
            # if nb_score exists
            if score_list:
                score_list[0].commute_score = commute_dict[neighborhood]
                score_list[0].save()
                print('updated commute', nb_obj)
            else:
                # create nb_score
                nb_obj = Neighborhood.objects.get(name=neighborhood)
                score_list = Score.objects.create(
                    neighborhood=nb_obj,
                    night_life_score=0,
                    commute_score=commute_dict[neighborhood],
                    crime_score=0,
                    noise_score=0,             
                )
                print('created commute obj', score_list)
        else:
            print("didn't find nb_obj: ", neighborhood)

    return True
    print ("Done")

def run():
    commute = get_commute_stats(params, destinations,nb_zip, api)
    update_commute_score(commute)

































## --------------------------------------------------------------------------------------------------------------- ##

'''
SAMPLE = 
https://maps.googleapis.com/maps/api/distancematrixjson?origins=West+Villiage|New+York+City&destinations=Oakhurts+NJ&key=AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM

MULTIPLE SAMPLE = 
https://maps.googleapis.com/maps/api/distancematrix/json?origins=75+9th+Ave+New+York,+NY&destinations=Bridgewater+Commons,+Commons+Way,+Bridgewater,+NJ|The+Mall+At+Short+Hills,+Morris+Turnpike,+Short+Hills,+NJ|Monmouth+Mall,+Eatontown,+NJ|Westfield+Garden+State+Plaza,+Garden+State+Plaza+Boulevard,+Paramus,+NJ|Newport+Centre+Mall,+Jersey+City,+NJ&departure_time=1541202457&traffic_model=best_guess&key=AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM


origins = can be multiple
destinations = can be multiple
mode = driving, walking, bicycling, transit, 
units=imperial
traffic_model = best_guess, pessimistic
transit_mode = bus, rail **need to have mode=transit for this to work**
KEY = AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM


LINK = https://maps.googleapis.com/maps/api/distancematrix/json?origins=upper+west+side+NY|New+York&destinations=956+east+8th+street+Brooklyn|New+York&mode=walking&units=imperial&key=AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM


RESPONSE = 

{
   "destination_addresses" : [ "956 E 8th St, Brooklyn, NY 11230, USA" ],
   "origin_addresses" : [
      "Upper West Side, New York, NY, USA",
      "West Village, New York, NY, USA",
      "Jersey City, NJ, USA"
   ],
   "rows" : [
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "12.9 mi",
                  "value" : 20723
               },
               "duration" : {
                  "text" : "1 hour 2 mins",
                  "value" : 3700
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "9.7 mi",
                  "value" : 15627
               },
               "duration" : {
                  "text" : "51 mins",
                  "value" : 3031
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "15.9 mi",
                  "value" : 25533
               },
               "duration" : {
                  "text" : "1 hour 12 mins",
                  "value" : 4335
               },
               "status" : "OK"
            }
         ]
      }
   ],
   "status" : "OK"
}
'''


# built in to the requests library
# for place in neighborhoods:
#    place = place.replace(" ", "+")
#    place = place.replace("'", "\'")
#    new_neighborhoods.append(place)

# # print (new_neighborhoods)

# # can change this value to start where we want 
# i = 0

# for i in range(0,188): 
#    # Origins=new_neighborhoods[i]+"+NY|"+new_neighborhoods[i+1]+"+NY|"+new_neighborhoods[i+2]+"+NY|"+new_neighborhoods[i+3]+"+NY|"+new_neighborhoods[i+4]+"+NY|"+new_neighborhoods[i+5]+"+NY|"+new_neighborhoods[i+6]
#    Origins=new_neighborhoods[i]+"+NY"
#    Destinations=destinations[0]+destinations[1]+destinations[2]+destinations[3]
#    Mode="transit"
#    Units="imperial"
#    Traffic_model="pessimistic"
#    Transit_mode="rail"
#    KEY="AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM"

#    LINK = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+Origins+"&destinations="+Destinations+"&mode="+Mode+"&units="+Units+"&key="+KEY
#    requests.get
#    print (LINK)

# i += 1





