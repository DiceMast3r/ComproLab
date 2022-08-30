print(" *** Maximum value ***")
list = [float(x) for x in input("Enter some numbers: ").split()]
list.sort()
n_out = list[-1]
if n_out % 1 == 0 or n_out % 1 == -0:
    n_out = int(n_out)
print("Max value = {0}".format(n_out))