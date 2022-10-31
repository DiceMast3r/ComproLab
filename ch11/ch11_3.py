tup = ("Fusce", "vehicula", "mattis", "eleifend", "condimentum", "nisl", "sit", "amet", "magna", "semper", 
        "pharetra", "Proin", "aliquet", "magna", "non", 'dapibus', "blandit", "Quisque", "nibh")
print(" *** Tuple Search ***")
x = input("Enter a word : ").split()
print()
if x[0] in tup:
    print("Index of word '{0}' is {1}".format(x[0], tup.index(x[0])))
else:
    print("Word '{0}' not found in Tuple".format(x[0]))