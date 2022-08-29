print(" *** Min Max Avg ***")
input = [int(x) for x in input("Enter 3 numbers : ").split()]
input.sort() #ใช้ sorted แล้วบัคแดก
print("min, mid, max ==> {0:.1f}, {1:.1f}, {2:.1f}".format(input[0], input[1], input[2]))
print("Average ==> {0:.2f}".format(sum(input) / len(input)))