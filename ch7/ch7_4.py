text_in = input("Enter query name and guest list: ").title()
print(' --- searching ---')
a = text_in.split()
if a[0] in a[1:]:
    print("Welcome, you're on the list!" ,a[0])
else:
    print("Sorry, you're not on the list!" ,a[0])