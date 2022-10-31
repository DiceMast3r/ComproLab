#print("*** Maximum Occurrence ***")
print("*** Minimum Occurrence ***")
lst = input("Enter some numbers: ").split()
lst = [int(i) for i in lst]
'''max = 0
for i in range(len(lst)):  # check for occurrence of each number
    if lst.count(lst[i]) > max:
        max = lst.count(lst[i])
        num = lst[i]
print(num)'''
# check for minimum occurrence
min_x = len(lst)
num = 0
for i in range(len(lst)): 
    if lst.count(lst[i]) < min_x:
        min_x = lst.count(lst[i])
        num = lst[i]
    elif lst.count(lst[i]) == min_x:
        print(min(lst, key=lst.count))
        #quit()
print(num)
