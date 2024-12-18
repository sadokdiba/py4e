tot = 0.0
count = 0
while True:
    value_entered = input('Enter number: ')
    if value_entered == 'done':
        break
    elif value_entered == 'exit':
        print('Program ended')
        quit()
    try:
        f_value_entered = float(value_entered)
    except:
        print('Invalid value')
        continue
    count += 1
    tot += f_value_entered
print(tot,count,tot/count)