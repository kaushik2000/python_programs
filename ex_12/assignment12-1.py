# Scraping Numbers from HTML using BeautifulSoup 
# In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py.
# The program will use urllib to read the HTML from the data files below, and parse the data,
#  extracting numbers and compute the sum of the numbers in the file.

# We provide two files for this assignment. 
# One is a sample file where we give you the sum for your testing and
# the other is the actual data you need to process for the assignment.

# Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_786838.html (Sum ends with 82)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignoring SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Getting the Html page
url = input("Enter - ")
html = urllib.request.urlopen(url, context = ctx).read()

# Parsing the html file and extracting all <span> tags
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

# Extracting the numbers from the span tags using contents()
numbers = list()
for tag in tags :
    if tag.contents :
        numbers.append(tag.contents[0])
#print(numbers)

# Finding the sum and count of all numbers in the list
total = 0
count = 0
for number in numbers :
    number = int(number)
    total += number
    count += 1
print("Count", count)
print("Sum", total)