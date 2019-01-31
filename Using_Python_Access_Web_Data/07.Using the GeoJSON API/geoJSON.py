
# Calling a JSON API

# In this assignment you will write a Python program somewhat similar to
# http://www.pythonlearn.com/code/geojson.py. The program will prompt for
# a location, contact a web service and retrieve JSON for the web service
# and parse that data, and retrieve the first place_id from the JSON.
# A place ID is a textual identifier that uniquely identifies a place as
# within Google Maps.
#
# API End Points
#
# To complete this assignment, you should use this API endpoint that has
# a static subset of the Google Data: http://python-data.dr-chuck.net/geojson
#
# This API uses the same parameters (sensor and address) as the Google API.
# This API also has no rate limit so you can test as often as you like.
# If you visit the URL with no parameters, you get a list of all of the
# address values which can be used with this API.
# To call the API, you need to provide a sensor=false parameter and the
# address that you are requesting as the address= parameter that is
# properly URL encoded using the urllib.urlencode() fuction
# as shown in http://www.pythonlearn.com/code/geojson.py

#Enter location: University of Connecticut
# Retrieving http://py4e-data.dr-chuck.net/json?address=University+of+Connecticut&key=42
# Retrieved 1813 characters
# Retrieving  http://py4e-data.dr-chuck.net/json?address=University+of+Connecticut&key=42
# Retrieved 1813 characters
# Place id ChIJC-MFejmK5okR6oVsKUtvbLI

C

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))
    #
    # lat = js['results'][0]['geometry']['location']['lat']
    # lng = js['results'][0]['geometry']['location']['lng']
    # print('lat', lat, 'lng', lng)
    # location = js['results'][0]['formatted_address']
    # print(location)


    # print json.dumps(js, indent=4)
    id = js['results'][0]['place_id']

    print ("Retrieving ", url)
    print ("Retrieved", len(data), "characters")
    print ("Place id", id)
