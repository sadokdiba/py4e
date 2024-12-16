tot = 0.0
count = 0
while True:
    vent = input('Enter number: ')
    if vent == 'done':
        break
    elif vent == 'exit':
        print('Program ended')
        quit()
    try:
        fvent = float(vent)
    except:
        print('Invalid value')
        continue
    count += 1
    tot += fvent
print(tot,count,tot/count)