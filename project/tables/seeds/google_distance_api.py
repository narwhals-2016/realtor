
import requests
import json

neighborhoods = ["Gravesend","Stapleton-Rosebank","Grasmere-Arrochar-Ft. Wadsworth","Grymes Hill-Clifton-Fox Hills","Old Town-Dongan Hills-South Beach","New Brighton-Silver Lake","New Dorp-Midland Beach","West New Brighton-New Brighton-St. George","Oakwood-Oakwood Beach","Westerleigh","Port Richmond","Borough Park","Great Kills","Todt Hill-Emerson Hill-Heartland Village-Ligh","Mariner's Harbor-Arlington-Port Ivory-Granite","Arden Heights","New Springville-Bloomfield-Travis","Rossville-Woodrow","Annadale-Huguenot-Prince's Bay-Eltingville","Charleston-Richmond Valley-Tottenville","Rosedale","Far Rockaway-Bayswater","Bensonhurst West","Springfield Gardens North","Springfield Gardens South-Brookville","Hammels-Arverne-Edgemere","Lindenwood-Howard Beach","Starrett City","East New York (Pennsylvania Ave)","East New York","Canarsie","Brownsville","Rugby-Remsen Village","Seagate-Coney Island","Breezy Point-Belle Harbor-Rockaway Park-Broad","Georgetown-Marine Park-Bergen Beach-Mill Basi","Flatlands","East Flatbush-Farragut","Madison brookl","Erasmus","Sheepshead Bay-Gerritsen Beach-Manhattan Beac","Crown Heights South","Prospect Lefferts Gardens-Wingate","Brighton Beach","Sunset Park East","Midwood","Homecrest","Flatbush","Ocean Parkway South","West Brighton","Kensington-Ocean Parkway","Windsor Terrace","Glen Oaks-Floral Park-New Hyde Park","Bellerose","Cambria Heights","Bath Beach","Douglas Manor-Douglaston-Little Neck","Queens Village","Laurelton","Oakland Gardens","Hollis","St. Albans","Jamaica Estates-Holliswood","Bayside-Bayside Hills","Fresh Meadows-Utopia","Auburndale","Dyker Heights","Ft. Totten-Bay Terrace-Clearview","Baisley Park","South Jamaica","Pomonok-Flushing Heights-Hillcrest","Jamaica","East Flushing","Briarwood-Jamaica Hills","Murray Hill","Kew Gardens Hills","Queensboro Hill queens","Sunset Park West","Flushing","South Ozone Park","Whitestone","Kew Gardens","Richmond Hill","Stuyvesant Town-Cooper Village","East Village","Greenpoint","Maspeth","Rego Park","Bay Ridge","SoHo-TriBeCa-Civic Center-Little Italy","Chinatown","Bensonhurst East","Forest Hills","Bushwick North","Fort Greene","Bedford brooklyn","Woodhaven","DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H","Bushwick South","Clinton Hill","Stuyvesant Heights nyc","Cypress Hills-City Line","Prospect Heights","Lower East Side","Ocean Hill","Ozone Park","Carroll Gardens-Columbia Street-Red Hook","Crown Heights North","Morningside Heights","Central Harlem South","Mott Haven-Port Morris","East Harlem North","Rikers Island","East Harlem South","North Side-South Side","Upper West Side","Yorkville nyc","Lincoln Square","Steinway","College Point","Old Astoria","Upper East Side-Carnegie Hill","East Elmhurst","hell's kitchen","Astoria","East Williamsburg","Lenox Hill-Roosevelt Island","Queensbridge-Ravenswood-Long Island City","Jackson Heights","North Corona","Midtown-Midtown South","Turtle Bay-East Midtown","Woodside","Hudson Yards-Chelsea-Flat Iron-Union Square","Corona","Murray Hill-Kips Bay","Williamsburg","Elmhurst-Maspeth","Gramercy","Elmhurst","West Village","Hunters Point-Sunnyside-West Maspeth","Pelham Bay-Country Club-City Island","Schuylerville-Throgs Neck-Edgewater Park","Co-Op City","Eastchester-Edenwald-Baychester","Westchester-Unionport","Battery Park City-Lower Manhattan","Allerton-Pelham Gardens","Parkchester","Pelham Parkway","Williamsbridge-Olinville","Bronxdale","Van Nest-Morris Park-Westchester Square","Woodlawn-Wakefield","West Farms-Bronx River","Soundview-Castle Hill-Clason Point-Harding Pa","Soundview-Bruckner","Glendale","Norwood","Belmont bronx","East Tremont","Crotona Park East","Bedford Park-Fordham North","Hunts Point","Longwood","Fordham South","Van Cortlandt Village","Claremont-Bathgate","Ridgewood","Kingsbridge Heights","Morrisania-Melrose","Mount Hope","North Riverdale-Fieldston-Riverdale","Spuyten Duyvil-Kingsbridge","Melrose South-Mott Haven North","East Concourse-Concourse Village","University Heights-Morris Heights","Marble Hill-Inwood","West Concourse","Brooklyn Heights-Cobble Hill","Highbridge","Washington Heights North","Washington Heights South","Central Harlem North-Polo Grounds","Hamilton Heights","Manhattanville","Middle Village"]
destinations = ["time+square+NYC|","union+square+NY|", "chamber+street+NY|", "59th+st+NY"]
# KEY="AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM"
KEY="AIzaSyA16dLy-Oi2VnSfWHgDugdS0bLc7afu8xI"
minutes = []

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
api = GoogleAPI(KEY)

# calls the api with the params for every origin 
for i in range(0,188): 
   params['origins']=neighborhoods[i]+"+NY"
   info = api.get('distancematrix/json', params=params)
   response_info = info.json()

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

   minutes.append(total_score_min)
   print(total_score_min)

print (minutes)


# minutes = [51.487, 77.092, 69.688, 73.292, 73.708, 75.008, 89.175, 70.258, 123.846, 89.692, 80.171, 47.325, 92.175, 105.833, 10.108, 105.017, 101.267, 133.925, 99.975, 96.308, 69.9, 89.45, 48.592, 70.95, 55.312, 71.733, 71.5, 22.762, 54.55, 61.421, 54.317, 46.013, 0, 53.771, 10.108, 69.775, 62.75, 47.775, 51.913, 41.792, 70.088, 37.408, 10.108, 50.346, 44.396, 48.754, 50.121, 36.496, 42.746, 78.958, 46.163, 41.846, 84.946, 62.867, 76.075, 55.792, 72.004, 62.0, 66.833, 72.85, 61.929, 60.467, 10.108, 71.371, 60.788, 53.837, 60.408, 69.154, 76.5, 61.233, 52.454, 57.746, 54.421, 42.092, 15.067, 56.25, 18.108, 44.396, 50.225, 72.183, 61.754, 50.2, 55.242, 13.213, 19.55, 31.854, 53.033, 42.996, 58.112, 12.867, 16.717, 48.592, 32.154, 41.296, 30.708, 38.467, 53.525, 23.996, 41.296, 30.454, 13.946, 44.837, 31.337, 25.329, 53.275, 43.658, 39.138, 37.408, 29.113, 55.221, 40.096, 30.029, 60.717, 30.029, 58.746, 23.321, 23.704, 19.754, 39.679, 69.667, 52.479, 23.488, 47.521, 18.688, 26.954, 31.85, 19.062, 20.496, 42.275, 32.433, 16.587, 25.925, 32.421, 10.113, 39.708, 11.887, 25.517, 45.192, 78.263, 39.737, 14.567, 19.425, 58.004, 81.592, 67.921, 50.558, 48.104, 21.054, 49.621, 57.504, 47.7, 49.592, 48.483, 51.879, 47.312, 46.5, 10.108, 53.671, 62.592, 0, 54.0, 48.908, 40.708, 43.708, 59.017, 33.133, 48.742, 59.487, 53.425, 38.275, 49.967, 37.521, 0, 60.188, 49.967, 39.583, 29.092, 40.175, 48.362, 27.325, 29.192, 40.508, 32.279, 32.279, 10.108, 32.329, 32.413, 56.9]




'''
KEY = AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM

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





