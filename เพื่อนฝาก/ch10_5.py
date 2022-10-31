a = {'egg' : 1, 'ham' : 1, 'water' : 1, 'soda' : 1}
print('*** Shopping List 2 ***')
x = input('Enter some pairs of (operation, item): ').split(',')
for op in x :
    b = op.split()
    command = b[0]
    item = b[1].lower()
    if command == 'a':
        if item not in a:
            a[item] = 1
        else:
            a[item] += 1
    elif command == 'r':
        if item in a:
            if a[item] <= 1:
                a.pop(item, None)
            else:
                a[item] -= 1
    else:
        print('Operation not supported!')
        exit(0)
print('Final shopping dict is', a)