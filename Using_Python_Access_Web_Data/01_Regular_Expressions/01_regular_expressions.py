import re
fhandl = open('regex_sum_177103.txt')
num = list()
for line in fhandl:
    line.rstrip()
    num+=(re.findall('[0-9]+', line))

# print (num)
total = 0
for nu in num:
    total +=int(nu)
print total