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
Duration and Distance in Rows in Json objects
'''



Origins="upper+west+side+NY|west+villiage+NY|Jersy+city+NJ"
Destinations="956+east+8th+street+Brooklyn" 
Mode="transit"
Units="imperial"
Traffic_model="pessimistic"
Transit_mode="rail"
KEY="AIzaSyCnE-5U0r-VELpWxXFXSfzwa6xWsC83hyM"

LINK = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+Origins+"&destinations="+Destinations+"&mode="+Mode+"&units="+Units+"&key="+KEY

print (LINK)



'''
RESPONSE = 

{
   "destination_addresses" : [ "956 E 8th St, Brooklyn, NY 11230, USA" ],
   "origin_addresses" : [
      "Upper West Side, New York, NY, USA",
      "West Village, New York, NY, USA"
   ],
   "rows" : [
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "13.2 mi",
                  "value" : 21249
               },
               "duration" : {
                  "text" : "40 mins",
                  "value" : 2393
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : [
            {
               "distance" : {
                  "text" : "9.0 mi",
                  "value" : 14548
               },
               "duration" : {
                  "text" : "27 mins",
                  "value" : 1647
               },
               "status" : "OK"
            }
         ]
      }
   ],
   "status" : "OK"
}

'''



