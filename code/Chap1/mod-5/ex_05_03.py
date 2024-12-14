hrs = input("Enter Hours: ")
hf = float(hrs)
r = input("Enter Rate: ")
rf= float(r)
a40 = float(40)
if hf <= a40:
    payl40 = hf * rf
    print(payl40)
else:
    payg40 = (a40 * rf) + ((hf-a40) * rf * 1.5)
    print (payg40)

# High-level calculation of pay
# def calculate_pay(hours, rate):
#     standard_hours = 40
#     overtime_multiplier = 1.5

#     if hours <= standard_hours:
#         total_pay = hours * rate
#     else:
#         overtime_hours = hours - standard_hours
#         total_pay = (standard_hours * rate) + (overtime_hours * rate * overtime_multiplier)
    
#     return total_pay

# # User input
# try:
#     hours = float(input("Enter Hours: "))
#     rate = float(input("Enter Rate: "))
#     pay = calculate_pay(hours, rate)
#     print(f"Total Pay: {pay}")
# except ValueError:
#     print("Invalid input. Please enter numeric values for hours and rate.")



