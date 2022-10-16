print("Sum Number in List")
lst = input("Input 5 Numbers : ").split()
lst = [int(i) for i in lst]
sum_num = 0
for num in lst:
    sum_num += num

print("Sum is {0}".format(sum_num))
