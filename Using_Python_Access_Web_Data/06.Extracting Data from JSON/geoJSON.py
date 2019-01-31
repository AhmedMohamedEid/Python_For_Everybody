
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
from urllib import request


url = input("Enter location: ")
if len(url) < 1: url = "http://py4e-data.dr-chuck.net/comments_177108.json"


data = request.urlopen(url).read()
comments = json.loads(data)["comments"]

counts = 0
for comment in comments:
  counts += int(comment['count'])

print ("Retrieving " + url)
print ("Retrieved " + str(len(data)) + " characters")
print ("Count: " + str(len(comments)))
print ("Sum: " + str(counts))

#Enter location: http://py4e-data.dr-chuck.net/comments_177108.json
# Retrieving http://py4e-data.dr-chuck.net/comments_177108.json
# Retrieved 2726 characters
# Count: 50
# Sum: 2647
