# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Use the file name mbox-short.txt as the file name
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
maxauther = dict()
for line in handle:
    line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    maxauther[words[1]] = maxauther.get(words[1] , 0 ) + 1
#print (maxauther)

largest = None
largest_auther = None

for key in maxauther:
    if largest is None :
        largest = maxauther[key]
    if largest < maxauther[key] :
        largest = maxauther[key]
        largest_auther = key
print (largest_auther,largest)



# ############# OutPut   ==
# cwen@iupui.edu 5
