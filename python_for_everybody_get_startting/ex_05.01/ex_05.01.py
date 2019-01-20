
num = 0
tot = 0.0
while True:
    sval = input ("Enter a Number: ")
    if sval == "done":  ## if user enter "done" Exit From this loop
        break
    try:   ## Check if the input is the float or string
        fval = float(sval)
    except:  ## if the input is string print this message and continue the Loop
        print("Invalid Input")
        continue
    print (fval)
    num +=1   # Number of iterations
    tot += fval  ## Compute the Total for all Number
print ("ALL DONE")
print (tot , num , tot/num)
