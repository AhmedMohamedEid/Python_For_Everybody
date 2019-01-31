
#
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_200535.json (Sum ends with 54)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format
# The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }


import json
# import xml.etree.ElementTree as ET
from urllib import request , parse
# import urllib

serviceUrl = "http://python-data.dr-chuck.net/geojson?"
while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceUrl + parse.urlencode({'sensor': 'false', 'address': address})
    data = request.urlopen(url).read()

    try: js = json.loads(data)
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    # print json.dumps(js, indent=4)
    id = js['results'][0]['place_id']

    print ("Retrieving ", url)
    print ("Retrieved", len(data), "characters")
    print ("Place id", id)

#
# # import urllib.request, urllib.parse, urllib.error
# import json
# import ssl
#
# # api_key = True
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + parse.urlencode(parms)
#
#     print('Retrieving', url)
#     uh = request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#
#     print(json.dumps(js, indent=4))
#
#     # id = js['results'][0]['place_id']
#     # print ("Retrieving ", url)
#     # print ("Retrieved", len(data), "characters")
#     # print ("Place id", id)
#     #
#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)



#Enter location: http://py4e-data.dr-chuck.net/comments_177108.json
# Retrieving http://py4e-data.dr-chuck.net/comments_177108.json
# Retrieved 2726 characters
# Count: 50
# Sum: 2647
