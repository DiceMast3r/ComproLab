" *** ตรงนี้ไปพิมเอง ***"
lst = input("Enter text : ").split()
dict = {}
for i in lst:
    dict[i] = lst.count(i)

#print(max(dict, key=dict.get))  #print the most frequent element
print("Max = {0} ==> {1}".format(max(dict, key=dict.get), dict[max(dict, key=dict.get)]))