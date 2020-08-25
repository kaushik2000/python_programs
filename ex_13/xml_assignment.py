# Extracting Data from XML

# In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
# The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, 
# compute the sum of the numbers in the file.

# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and 
# the other is the actual data you need to process for the assignment.

#   Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
#   Actual data: http://py4e-data.dr-chuck.net/comments_786840.xml (Sum ends with 23)

import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignoring SSL Errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




while True :
    # Getting url and XML page
    url = input("Enter the XML url: ")
    try:
        print("Retrieving", url)
        html = urllib.request.urlopen(url, context= ctx).read()
    except:
        break

    # Getting XML tree and a list of <comment> tag details from the file handle
    comment_info_tree = ET.fromstring(html)
    print("Retrieved", len(html), "characters")
    comment_tags = comment_info_tree.findall("comments/comment")

    # Calculating sum
    total = 0
    for comment_tag in comment_tags :
        count = comment_tag.find("count").text
        count = int(count)
        total = total + count
        print("Count:", count)
    print("Sum:", total)    
       