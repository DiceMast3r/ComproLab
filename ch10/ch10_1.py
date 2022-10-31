print(" *** Creating Dictionary ***")
x = input("Enter text : ").split(" ")
a = dict()
for i in range(0, len(x), 2):
    a[x[i]] = x[i+1]
print(a)