# Extracting Data from JSON

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:

# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#    Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#   Actual data: http://py4e-data.dr-chuck.net/comments_786841.json (Sum ends with 73)

import json
import urllib.request, urllib.parse, urllib.error
import ssl

site_url = "http://py4e-data.dr-chuck.net/"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    file = input('Enter the file to be accessed from the location \"{}\": '.format(site_url))
    if len(file) < 1 : continue

    url = site_url + file
    print("Retrieving", url)

    try:
        url_handle = urllib.request.urlopen(url, context=ctx)
    except:
        print('=== Failed to retrieve :', url, "===")
        continue
    
    data = url_handle.read().decode()
    print("Retrieved", len(data), "characters...")

    js_data = json.loads(data)
    comments = js_data['comments']

    total = 0
    for comment in comments :
        total = total + comment['count']

    print("Count:", len(comments))
    print("Sum:", total)
    