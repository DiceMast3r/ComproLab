print("Min Number in List")
list_in = input("Input Numbers : ").split()
list_in = [int(i) for i in list_in]
min_num = min(list_in)
print("Min number in List is {0}".format(min_num))