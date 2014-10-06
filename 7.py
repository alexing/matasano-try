#!/usr/bin/env python
import cryp

key='YELLOW SUBMARINE'

f = open('7.txt')
ciphertext = f.read() #FILE TO VARIABLE
ciphertext=cryp.base64ToHex(ciphertext) #Convert to hex
f.close()

print cryp.decodeAES_ECB(ciphertext,key)
