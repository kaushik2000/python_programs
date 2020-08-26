# Service oriented json with google geomaps API

import json
import urllib.request, urllib.parse, urllib.error

service_url = "https://maps.googleapis.com/maps/api/geocode/json?"

while True :
    address = input("Enter the address: ")
    if len(address) < 1 : break

    url = service_url + urllib.parse.urlencode( {"address" : address} ) # Use urllib.parse.urlencode() to add params[address]

    # Note Google is increasingly requiring API keys for this API 
    print("Retrieving:", url)
    url_handle = urllib.request.urlopen(url) # Get url handle using urllib.request.urlopen()
    data = url_handle.read().decode() # Decode to convert UTF-8 to UNICODE
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print("===Failed to retrieve data===")
        print(data)
        continue

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print('Location:', location)
