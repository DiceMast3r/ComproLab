def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)

    return result


text, n = input("Enter a word and a number: ").split()
n = int(n)
text = "testcipher"
n = 3
if n <= 0:
    print("Number must be between 1-26")
    exit()
#n = n * -1 inverse key
decrypted = decrypt(text, n)
print(decrypted.upper())
