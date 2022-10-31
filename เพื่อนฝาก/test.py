def decrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            """result += chr((ord(char) - s - 65) % 26 + 65)"""
            u_1 = ord(char)
            u_1 = u_1 - s
            u_1 = u_1 - 65
            u_1 = u_1 % 26
            u_1 = u_1 + 65
            result += chr(u_1)

        # Encrypt lowercase characters
        else:
            #result += chr((ord(char) - s - 97) % 26 + 97)
            l_1 = ord(char)
            l_1 = l_1 - s
            l_1 = l_1 - 97
            l_1 = l_1 % 26
            l_1 = l_1 + 97
            result += chr(l_1)

    return result


text, n = input("Enter a word and a number: ").split()
n = int(n)
if n <= 0:
    print("Number must be between 1-26")
    exit()
#n = n * -1 inverse key
decrypted = decrypt(text, n)
print(decrypted.upper())
