import matplotlib.pyplot as plt

#print("Income Expense test")
inp = input("Enter in pair (category1 value1,category2 value2,...): ").strip().split(",")
for i in range(len(inp)): # this loop removes the spaces
    inp[i] = inp[i].strip()
#print(inp)
dict = {}
for i in inp: # put data in dictionary
    x = i.split(" ")
    dict[x[0]] = x[1]
print(dict)
labels = []
sizes = []
for x, y in dict.items():
    labels.append(x)
    sizes.append(y)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.show()