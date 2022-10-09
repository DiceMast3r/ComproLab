n = input("Enter some words: ").split()
root = n[0].lower()
print("lowerCamelCase: " + root + ''.join(n.title() for n in n[1:]))