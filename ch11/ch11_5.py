cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}
x = input("Input ADFGX cipher text: ")
if len(x) % 2 == 1:
    print("FAILED TO DECRYPT")
    exit()
elif len(x) == 0:
    print("FAILED TO DECRYPT")
    exit()
elif x.isupper() == False:
    print("FAILED TO DECRYPT")
    exit()
# Check if x contains any characters other than A, D, F, G, X
for i in x:  # i is each character in x
    if i not in ('A', 'D', 'F', 'G', 'X'): 
        print("FAILED TO DECRYPT")
        exit()
else:
    a = []
    for i in range(0, len(x), 2): 
        a.append(x[i:i+2]) # Split x into pairs
    for j in a:
        print(cipher_key[tuple(j.upper())], end="") 
