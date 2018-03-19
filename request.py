# -*- coding: utf-8 -*-
import requests
import keys
import constants
from objects import Location

# This function get the latitude and longitude of an address through Google Geocoding API. 
# Return an object with the address, latitude and longitude. 
# https://developers.google.com/maps/documentation/geocoding/start
def geocoding(location_address):

    payload = {
        "address" : location_address,
        "key" : keys.GOOGLEAPI_KEY,
        "language" : "es",
        "region" : "es",
        "components" : "country:ES"
    }

    r = requests.get(url=constants.GEOCODEAPI_URL, params=payload)
    
    response = r.json()

    if response["status"] == "OK":
        lat = response["results"][0]["geometry"]["location"]["lat"]
        lng = response["results"][0]["geometry"]["location"]["lng"]
        address = response["results"][0]["formatted_address"]
    else:
        address = ''
        lat = 0
        lng = 0
    
    loc = Location(address, lat, lng)
    return loc


# This function get the weather of an address through DarkSky API. 
# The API only works with the coordinates (latitude and longitude) for this reason its necessary use the geocoding function.  
# https://darksky.net/dev/docs#forecast-request
def weather(location_query):

    location = geocoding(location_query)

    if len(location.address) != 0:

        latlong = str(location.latitude) + str(",") + str(location.longitude)
        
        url = constants.DARKSKYAPI_URL.format(keys.DARKSKY_KEY, latlong)

        payload = {
            "lang" : "es",
            "units" : "si",
            "exclude" : "minutely, hourly, daily"
        }

        r = requests.get(url=url, params=payload)

        response = r.json()
        #print r.url
        #print r.text
        print response['currently']['summary']
        print response['currently']['temperature']
        print response['currently']['precipProbability']

    else:
        response = ''

    return response


def weatherY(location):

    url = "https://query.yahooapis.com/v1/public/yql?"
    query = "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='{}') and u='c'"

    params = {
        "q" : query.format(location),
        "format" : "json"
    }

    r = requests.get(url=url, params=params)
    response = r.json()
    print r.url
    print r.text
    print '\n'
    location = response['query']['results']['channel']['location']

if __name__ == "__main__":
    weather('totana')