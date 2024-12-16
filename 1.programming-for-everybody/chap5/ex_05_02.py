lrgst = None
smlst = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        inum = int(num)
    except ValueError:
        print('Invalid input')
        continue
    if smlst is None or inum < smlst:
        smlst = inum
    if lrgst is None or inum > lrgst:
        lrgst = inum
print('Maximum',lrgst)
print('Minimum',smlst)

# print('Invalid input')
# print('Maximum is 10')
# print('Minimum is 2')