import random

pws = ["trevor", "password", "what", "ohnonotmypassword"]

encrypted_length = 20
encrypted_pws = {}
char_list = []

for i in range(33, 127):
    char = chr(i)
    char_list.append(char)

for p in range(0, len(pws)):
    encrypt = ""
    pw = pws[p]

    for i in range(0, encrypted_length):
        x = random.randint(0, len(char_list) - 1)
        encrypt += char_list[x]

    #print(f"Pasword: {pw} | Encryption: {encrypt}")

    encrypted_pws[pw] = encrypt

for x in encrypted_pws:

    print("Password: " + x + " -> Encrypted Password: " + (encrypted_pws[x]))


usrin = input("Password: ")


    

