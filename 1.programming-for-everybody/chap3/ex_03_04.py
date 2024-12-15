try:
    score = float(input("Enter Score between 0.0 and 1.0: "))
except:
    print("Entry not a numerical value")
    quit()   
if 1.0 > score >= 0.9 :
    print("A")
elif .9 > score >= .8:
    print("B")
elif .8 > score >= .7:
    print("C")
elif .7 > score >= .6:
    print("D")
elif .6 > score > .0:
    print("F")
else:
    print("Number Entered Out of range")                    


