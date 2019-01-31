
# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/geoxml.py. The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# Sample data: http://python-data.dr-chuck.net/comments_42.xml (Sum=2482)
# Actual data: http://python-data.dr-chuck.net/comments_200531.xml (Sum ends with 11)
# You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the assignment - so only use your own data url for analysis.
# Data Format and Approach
# The data consists of a number of names and comment counts in XML as follows:
# <comment>
#   <name>Matthias</name>
#   <count>97</count>
# </comment>
# You are to look through all the <comment> tags and find the <count> values sum the numbers. The closest sample code that shows how to parse XML is geoxml.py. But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.
# To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:
# counts = tree.findall('.//count')
# Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.
# Sample Execution



from urllib import request
import xml.etree.ElementTree as ET

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_177107.xml'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'
# Open File
xml_file=  request.urlopen(serviceurl).read()
# Read Xml File
tree = ET.fromstring(xml_file)
# get count Tag
counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))
accumul = 0

for count in counts:
    accumul += int(count.text)

print ("Sum:" + str(accumul))

# Out Put
# Count: 50
# Sum:2523
