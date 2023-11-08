# Encryption
# Taking PlainText And Key
print(":::::::::::::::::::::::::::::::::::::Encryption:::::::::::::::::::::::::::::::::::::::::::::::::::\n\n")
plaintext=input("Enter the message:-").lower()
e=0
while(e!=1):
    key=input("Enter the key:-")
    if len(key)<len(plaintext):
        e=1
    else :
        print("Key Should be smaller than Plaintext Length")


# Converting Key And Plaintext to Array
plaintextArray = [char for char in plaintext]
keyarray = [char for char in key]
keyarray1 = []
for i in range(0,len(plaintextArray)):
    keyarray1.append(keyarray[i%len(keyarray)])
print("Plaintext  :-",plaintextArray)
print("Vignere Key:-",keyarray1)

# Converting the key and plaintext to mapped values 

mapping = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "j",
    10: "k",
    11: "l",
    12: "m",
    13: "n",
    14: "o",
    15: "p",
    16: "q",
    17: "r",
    18: "s",
    19: "t",
    20: "u",
    21: "v",
    22: "w",
    23: "x",
    24: "y",
    25: "z"
}
plaintextnumber=[]
keynumber=[]
for i in range(0,len(plaintextArray)):
    plaintextnumber.append(mapping[plaintextArray[i]])
    keynumber.append(mapping[keyarray1[i]])

print("Plaintext Number  :-",plaintextnumber)
print("Vignere Key Number:-",keynumber)

# Performing Ecryption
ciphernumber=[]
for i in range(0,len(plaintextnumber)):
    sum = plaintextnumber[i] + keynumber[i]
    ciphernumber.append(sum%26)

print("Cipher Number:-",ciphernumber)

# Converting Cipher Number to Cipher Text
ciphertext=[]
for i in range(0,len(ciphernumber)):
    ciphertext.append(mapping[ciphernumber[i]])
print("Cipher Text:-",ciphertext)

# Decryption
print(":::::::::::::::::::::::::::::::::::::Decryption:::::::::::::::::::::::::::::::::::::::::::::::::::\n\n")

print("Cipher Number:-",ciphernumber)
print("Vignere Key Number:-",keynumber)

#Decrytion of Ciphertext
plaintextnumberafterDecryption=[]
for i in range(0,len(ciphernumber)):
    difference = ciphernumber[i]-keynumber[i]
    if difference<0:
        difference = 26 + difference
    plaintextnumberafterDecryption.append(difference%26)

print("Plaintext Number After Dcryption:-",plaintextnumberafterDecryption)

#Plainttext number to Plaintext
plaintextafterDecryption=[]
for i in range(0,len(plaintextnumberafterDecryption)):
    plaintextafterDecryption.append(mapping[plaintextnumberafterDecryption[i]])

print("PlainText After Decryption:-",plaintextafterDecryption)
