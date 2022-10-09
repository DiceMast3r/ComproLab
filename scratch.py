print("*** Maximum Occurrence ***")
lst = input("Enter some numbers: ").split()
lst = [int(i) for i in lst]
max = 0
for i in range(len(lst)):   #check for occurrence of each number
    if lst.count(lst[i]) > max:
        max = lst.count(lst[i])
        num = lst[i]
print(num)



