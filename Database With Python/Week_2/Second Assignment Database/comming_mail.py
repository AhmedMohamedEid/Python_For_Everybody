
import sqlite3
# Connecting to the file in which we want to store our db
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Deleting any possible table that may affect this assignment
cur.execute('''
DROP TABLE IF EXISTS Counts''')

#Creating the table we're going to use
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

#Indicating the file (URL in this case) from where we'll read the data
# fname = "http://www.pythonlearn.com/code/mbox.txt"
# fh = urllib.request.urlopen(fname)
# open File
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)

#Reading each line of the file
for line in fh:
    #Finding an email address and splitting it into name and organization
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    (emailname, organization) = email.split("@")
    print (email)

    #Updating the table with the correspondent information
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (organization, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES ( ?, 1 )''', ( organization, ) )
    else :
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
            (organization, ))

# We commit the changes after they've finished because this speeds up the
# execution and, since our operations are not critical, a loss wouldn't suppose
# any problem
conn.commit()

# Getting the top 10 results and showing them
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print
print ("Counts:")
for row in cur.execute(sqlstr) :
    print (str(row[0]), row[1])

#Closing the DB
cur.close()
