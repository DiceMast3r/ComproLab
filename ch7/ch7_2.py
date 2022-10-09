print(" *** Remove ODD characters ***")
text_in = input("Enter a string : ")
list_txt = list(text_in)
list_odd = []
for i in range(len(list_txt)):
    if i % 2 != 0:
        list_odd.append(list_txt[i])
print("Even characters = ", *list_odd, sep="") # *list_odd is a list unpacking