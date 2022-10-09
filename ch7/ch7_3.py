print(" *** Palindrome Checker ***")
text_in = input("Input 3 word to check: ").split()
a = len(text_in[0])
b = len(text_in[1])
c = len(text_in[2])
if a <= 1 or b <= 1 or c <= 1:
    print("Input Error")
    exit()
for i in text_in:
    if i != i[::-1]:
        print("{0} not palindrome".format(i))
    else:
        print("{0} is palindrome".format(i))
