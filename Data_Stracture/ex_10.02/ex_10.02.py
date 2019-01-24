# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Use the file name mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
hour = dict()
for line in handle:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    hour[words[5]] = hour.get(words[5] , 0 ) + 1
#print (hour)

hour2 = dict()
for key in hour.keys():
    key.split(":")
    hour2[key[0:2]] = hour2.get(key[0:2],0)+1
#print (hour2)


lst = []

for a,b in hour2.items():
    lst.append((a,b))

lst.sort()

for a,b in lst:
    print (a,b)



# ############# OutPut   ==
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
