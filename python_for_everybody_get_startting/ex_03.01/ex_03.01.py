 #  Write a program to prompt the user for hours and rate per hour using input to
 #  compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
 #  the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
 #  of 10.50 per hour to test the program (the pay should be 498.75). You should
 #  use input to read a string and float() to convert the string to a number.
 #  Do not worry about error checking the user input - assume the user types
 #  numbers properly.

hrs = input("Enter Hours:")
re = input("Enter Rate:")
h = float(hrs) #  h = 45
r = float(re)   # r = 10.5
if h > 40 :
    reg = h*r # = 45*10.5 = 472.5
    otp = (h-40)*(r*.5)  # (45-40)*(10.5*.5)= 5*5.25 = 26.25

    xp = reg+otp # 472.5 + 26.25= 498.75
else:
    xp = h*r   #  45*10.5 = 472.5
print(xp)
