x = input("Enter : ").split()
dict_old = {'Volkswagan': 1, 'Toyota': 2, 'Tesla': 2}
dict_new = dict_old.copy()
print("dict_old =", dict_old)
for i in range(0, len(x), 2):
    if x[i] in dict_old:
        print("{0} exists in dicts".format(x[i]))
        dict_new[x[i]] += int(x[i+1])
    else:
        print("{0} does not exist".format(x[i]))
        dict_new[x[i]] = int(x[i+1])
print("dict_new =", dict_new)
