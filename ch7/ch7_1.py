print(" *** Alphabet classification ***")
text_in = input("Input Sentence to count : ")
print()
text_in = text_in.lower()
count = 0
for i in text_in:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
print("Vovel in this sentence is", count)
print("Consonant in this sentence is", len(text_in) - count)
