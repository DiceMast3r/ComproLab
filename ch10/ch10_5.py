print(" *** Creating Dictionary ***")
x = input("Enter text : ").split(" ")
a = dict()
for i in range(0, len(x), 2):
    if x[i] in a:
        a[x[i]] += int(x[i+1])
    else:
        a[x[i]] = int(x[i+1])
print(a)