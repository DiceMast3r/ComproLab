import json

lst = json.loads(input())
chk_odd = []
for i in lst:
    if i % 2 == 0:
        print(i)
    else:
        chk_odd.append(i)
if len(chk_odd) == len(lst):
    print("Nope")
