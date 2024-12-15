def computepay(hours, rate):
    overtime_multiplier=1.5
    standard_hours=40
    overtime_calculator= (hours-standard_hours)*rate*overtime_multiplier
    if hours <= 40:
        pay=hours*rate
    else:
        pay = standard_hours*rate + overtime_calculator 
    return pay
try:
    hours = float(input("Enter Hours:"))
    rate = float(input("Enter Rate: "))
    pay = computepay(hours,rate)
    print("Pay", pay)
except ValueError:
    print("Enter a numerical value!")
    
