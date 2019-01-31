
# '''
# Following Links in Python
# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.
# We provide two files for this assignment. One is a sample file where we give you the name for your testing and the other is the actual data you need to process for the assignment
# Sample problem: Start at http://python-data.dr-chuck.net/known_by_Fikret.html
# Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
# Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
# Last name in sequence: Anayah
# Actual problem: Start at: http://python-data.dr-chuck.net/known_by_Blanka.html
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
# Hint: The first character of the name of the last page that you will load is: L
# '''

from urllib import request
from bs4 import BeautifulSoup

url = input('Enter URL : ')
count = int(input("Enter Count: "))
position = int(input("Enter Position:"))

for i in range(count):
    html= request.urlopen(url).read()
    soup = BeautifulSoup(html,'html5lib')

    tags = soup('a')
    linkes_url = []
    name = []
    for tag in tags:
        x = tag.get('href', None)
        linkes_url.append(x)
        y = tag.text
        name.append(y)

    print (linkes_url[position-1])
    print (name[position-1])
    url = (linkes_url[position-1])
