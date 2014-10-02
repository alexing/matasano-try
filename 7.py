#!/usr/bin/env python
import cryp
from Crypto.Cipher import AES

key='YELLOW SUBMARINE'

f = open('7.txt')
ciphertext = f.read() #FILE TO VARIABLE
ciphertext=cryp.base64ToHex(ciphertext) #Convert to hex
f.close()

cipher = AES.new(key, AES.MODE_ECB)
plaintext=cipher.decrypt(ciphertext)
print plaintext
