
import requests
import json

neighborhoods = ["Gravesend","Stapleton-Rosebank","Grasmere-Arrochar-Ft. Wadsworth","Grymes Hill-Clifton-Fox Hills","Old Town-Dongan Hills-South Beach","New Brighton-Silver Lake","New Dorp-Midland Beach","West New Brighton-New Brighton-St. George","Oakwood-Oakwood Beach","Westerleigh","Port Richmond","Borough Park","Great Kills","Todt Hill-Emerson Hill-Heartland Village-Ligh","Mariner's Harbor-Arlington-Port Ivory-Granite","Arden Heights","New Springville-Bloomfield-Travis","Rossville-Woodrow","Annadale-Huguenot-Prince's Bay-Eltingville","Charleston-Richmond Valley-Tottenville","Rosedale","Far Rockaway-Bayswater","Bensonhurst West","Springfield Gardens North","Springfield Gardens South-Brookville","Hammels-Arverne-Edgemere","Lindenwood-Howard Beach","Starrett City","East New York (Pennsylvania Ave)","East New York","Canarsie","Brownsville","Rugby-Remsen Village","Seagate-Coney Island","Breezy Point-Belle Harbor-Rockaway Park-Broad","Georgetown-Marine Park-Bergen Beach-Mill Basi","Flatlands","East Flatbush-Farragut","Madison","Erasmus","Sheepshead Bay-Gerritsen Beach-Manhattan Beac","Crown Heights South","Prospect Lefferts Gardens-Wingate","Brighton Beach","Sunset Park East","Midwood","Homecrest","Flatbush","Ocean Parkway South","West Brighton","Kensington-Ocean Parkway","Windsor Terrace","Glen Oaks-Floral Park-New Hyde Park","Bellerose","Cambria Heights","Bath Beach","Douglas Manor-Douglaston-Little Neck","Queens Village","Laurelton","Oakland Gardens","Hollis","St. Albans","Jamaica Estates-Holliswood","Bayside-Bayside Hills","Fresh Meadows-Utopia","Auburndale","Dyker Heights","Ft. Totten-Bay Terrace-Clearview","Baisley Park","South Jamaica","Pomonok-Flushing Heights-Hillcrest","Jamaica","East Flushing","Briarwood-Jamaica Hills","Murray Hill","Kew Gardens Hills","Queensboro Hill","Sunset Park West","Flushing","South Ozone Park","Whitestone","Kew Gardens","Richmond Hill","Stuyvesant Town-Cooper Village","East Village","Greenpoint","Maspeth","Rego Park","Bay Ridge","SoHo-TriBeCa-Civic Center-Little Italy","Chinatown","Bensonhurst East","Forest Hills","Bushwick North","Fort Greene","Bedford","Woodhaven","DUMBO-Vinegar Hill-Downtown Brooklyn-Boerum H","Bushwick South","Clinton Hill","Stuyvesant Heights","Cypress Hills-City Line","Prospect Heights","Lower East Side","Ocean Hill","Ozone Park","Carroll Gardens-Columbia Street-Red Hook","Crown Heights North","Morningside Heights","Central Harlem South","Mott Haven-Port Morris","East Harlem North","Rikers Island","East Harlem South","North Side-South Side","Upper West Side","Yorkville","Lincoln Square","Steinway","College Point","Old Astoria","Upper East Side-Carnegie Hill","East Elmhurst","Clinton","Astoria","East Williamsburg","Lenox Hill-Roosevelt Island","Queensbridge-Ravenswood-Long Island City","Jackson Heights","North Corona","Midtown-Midtown South","Turtle Bay-East Midtown","Woodside","Hudson Yards-Chelsea-Flat Iron-Union Square","Corona","Murray Hill-Kips Bay","Williamsburg","Elmhurst-Maspeth","Gramercy","Elmhurst","West Village","Hunters Point-Sunnyside-West Maspeth","Pelham Bay-Country Club-City Island","Schuylerville-Throgs Neck-Edgewater Park","Co-Op City","Eastchester-Edenwald-Baychester","Westchester-Unionport","Battery Park City-Lower Manhattan","Allerton-Pelham Gardens","Parkchester","Pelham Parkway","Williamsbridge-Olinville","Bronxdale","Van Nest-Morris Park-Westchester Square","Woodlawn-Wakefield","West Farms-Bronx River","Soundview-Castle Hill-Clason Point-Harding Pa","Soundview-Bruckner","Glendale","Norwood","Belmont","East Tremont","Crotona Park East","Bedford Park-Fordham North","Hunts Point","Longwood","Fordham South","Van Cortlandt Village","Claremont-Bathgate","Ridgewood","Kingsbridge Heights","Morrisania-Melrose","Mount Hope","North Riverdale-Fieldston-Riverdale","Spuyten Duyvil-Kingsbridge","Melrose South-Mott Haven North","East Concourse-Concourse Village","University Heights-Morris Heights","Marble Hill-Inwood","West Concourse","Brooklyn Heights-Cobble Hill","Highbridge","Washington Heights North","Washington Heights South","Central Harlem North-Polo Grounds","Hamilton Heights","Manhattanville","Middle Village"]
destinations = ["time+square+NYC|","union+square+NY|", "chamber+street+NY|", "59th+st+NY"]
KEY="AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM"

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
for i in range(0,1): 
   params['origins']=neighborhoods[i]+"+NY"
   info = api.get('distancematrix/json', params=params)
   response_info = info.json()

   dest = 0
   print(response_info["rows"][0]["elements"][dest]["duration"]["text"])










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





