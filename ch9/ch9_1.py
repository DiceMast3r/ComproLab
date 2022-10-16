colorList = ['yellow', 'red', 'green', 'black', 'brown', 'grey']
print(" *** Find word start with character ***")
print(colorList)
element = input("Enter your character : ")
found_list = []
for i in colorList:
    if element in i[0]:
        found_list.append(i)
if len(found_list) != 0:
    print(found_list)
    exit()
else:
    print("There is no element start with '{0}'".format(element))
    exit()