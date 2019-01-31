import urllib.request , urllib.parse , urllib.error
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'
# serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    #add the parameters needed to the url  'sensor':'false',
    url = serviceurl + urllib.parse.urlencode({'address': address})
    print ('Retrieving',url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print ('Retrieved', len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None
    if not js or 'status' not in js or js['status'] != 'Ok':
        print('======  Failure To Retrieve ======')
        print (data)
        continue

    #print the response, enable for debug
    print (json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    #extract place_id
    # place_id = js["results"][0]['place_id']
    # print (place_id)
