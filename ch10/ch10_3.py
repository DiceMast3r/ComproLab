print(" *** Find least frequent word ***")
lst = input("Enter text : ").split()
dict = {}
for i in lst:
    dict[i] = lst.count(i)

#print(max(dict, key=dict.get))  #print the most frequent element
#print(min(dict, key=dict.get))  #print the least frequent element
print("Least = {0} => {1}".format(min(dict, key=dict.get), dict[min(dict, key=dict.get)]))