print(" *** Greeting ***")
list = input("Enter some names: ").split()
print(list)
for i in list:
    print("Hello {0}".format(i))