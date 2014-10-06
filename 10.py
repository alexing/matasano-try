#!/usr/bin/env python
import cryp

#Testing our encrypting and decrypting functions
myMessage="Eh guacho puto te vamo a achurar y te vamo a roba' la llantas ah"
myKey="TUVIEJA EN TANGA"
myIV="\x04"*16
#Is our ECB encrypt function ok?
cipher=cryp.encodeAES_ECB(myMessage,myKey)
plain=cryp.decodeAES_ECB(cipher,myKey)
assert(myMessage==plain)

#Is our CBC encrypt function ok?
cipher=cryp.encodeAES_CBC(myMessage,myKey,myIV)
plain=cryp.decodeAES_CBC(cipher,myKey,myIV)
assert(myMessage==plain)
#Alright, let's begin


key="YELLOW SUBMARINE"
iv="\x00"*16
f = open('10.txt')
cipher = f.read() #FILE TO VARIABLE
cipher=cryp.base64ToHex(cipher) #Convert to hex
f.close()

plain=cryp.decodeAES_CBC(cipher,key,iv)
print plain.decode()