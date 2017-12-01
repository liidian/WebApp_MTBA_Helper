import urllib.request   # urlencode function
import json
import pprint
# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    new_place =""
    for i in place_name:
        if i == " ":
            new_place += "+"
        else:
            new_place += i
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + new_place
    # print (url)
    # print(d)
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response = json.loads(response_text)
    print(response["results"][0]["formatted_address"])
    # for i in range (len(response["results"])):
    #     print(response["results"][i]["formatted_address"])

    try:   
        lat = (response["results"])[0]["geometry"]["location"]["lat"]
        lng = (response["results"])[0]["geometry"]["location"]["lng"]
        print (lat, lng)
        return lat, lng
    except:
        print ("You tried too many times. Please wait and try again")

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.
    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API in 'MBTA-realtime API v2 Documentation'.
    """
    d = {}
    k = 0
    apikey = "wX9NwuHnZU2ToO7GmGR9uw"
    params = ("api_key=" + apikey +
             "&lat=" + str(latitude) +
             "&lon=" + str(longitude) +
             "&format=json")

    url = "http://realtime.mbta.com/developer/api/v2/stopsbylocation?%s" % params

    
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    p = json.loads(response_text)
    # return p
    name = p["stop"][0]['stop_name']
    distance = float(p["stop"][0]['distance'])
    distance = round (distance, 3)
    # for i in range (len(p['stop'])):
    #     print (p["stop"][i]['stop_name'], p["stop"][i]['distance'])

    return name, distance


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and the 
    distance from the given place to that stop.
    """
    try:
        lat, lng = get_lat_long(place_name)
        return get_nearest_station (lat, lng)
    except:
        return "There is no stations within 1 mile radius"


# print (get_lat_long ("Babson College"))
# print (get_nearest_station (42.2993708,-71.2659951))
# print (find_stop_near("Babson College"))
# print (find_stop_near("Back Bay"))