import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL Certificate errors
cert_deal = ssl.create_default_context()
cert_deal.check_hostname = False
cert_deal.verify_mode = ssl.CERT_NONE

# Get url from user (.html file)
url = input("Enter URL - ")
# Get the html page from thge url
html = urllib.request.urlopen(url, context = cert_deal).read()
print(html)

# Parse the obtained page to clean all extra sequences
soup = BeautifulSoup(html, 'html.parser')
print(soup)

# Retrieve all anchor tags
tags = soup('a') # Creates a list of all anchor tags (<a>) from the obtained html-soup
print(tags)

# Getting the link by treating it as a dict() with key as 'href'
for tag in tags :
    print(tag.get('href', None))