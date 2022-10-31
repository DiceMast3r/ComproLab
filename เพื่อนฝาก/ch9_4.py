print("*** Shopping List ***")
lst = ['egg', 'ham', 'water', 'soda']
inp = input('Enter some pairs of (operation, item): ').split(',')
for pair in inp:
    op, item = pair.split()
    item = item.lower()
    if op == 'a':
        if lst.count(item) <= 0:
            lst.append(item.lower())
        elif lst.count(item) > 0:
            #print('Item already exists!')
            continue
    elif op == 'r':
        if lst.count(item) > 0:
            lst.remove(item)
        elif lst.count(item) <= 0:
            #print('Item does not exist!')
            continue
    else:
        print('Operation not supported!')
        quit()
print('Final shopping list is', lst)