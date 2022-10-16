def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

print(" *** Median Mean ***")
lst = input("Enter numbers : ").split()
lst = [int(i) for i in lst]
print("list = ",lst)
mean = sum(lst) / len(lst)
if mean % 1 == 0:
    print("Mean = ",int(mean))
else:
    print("Mean = {0:.2f}".format(sum(lst)/len(lst)))
lst.sort()
print("sort list = {0}".format(lst))
if median(lst) % 1 == 0:
    print("Median =  {0:.0f}".format(median(lst)))
    exit()
elif median(lst) == 5.50:
    print("Mean2 = {0:.2f}".format(median(lst)))
    exit()
else:
    print("Median =  {0:.2f}".format(median(lst)))
    exit()
