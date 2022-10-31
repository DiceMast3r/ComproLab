n = int(input())
lst = []
lst_2 = []
for i in range(1, n):
    lst.append(int(input()))
lst.sort()
for j in range(0, lst[-1]):
    if j not in lst:
        lst_2.append(j)
for k in lst_2:
    print(k)
