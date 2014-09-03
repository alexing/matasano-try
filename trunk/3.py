#!/usr/bin/env python
import binascii
import string
from cryp import hexToBin, extendIntInBin, XOR

encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
encodedBin=hexToBin(encoded)

f=open("out.txt","w+")

for i in xrange(0x00,0xFF):
	auxString=extendIntInBin(i,len(encodedBin))
	xor=XOR(auxString,encodedBin,2)
	if len(xor)%2==0: #Not nice but works. Some lines don't have an odd number of characters and script implodes. 
			if all(char in string.printable for char in binascii.unhexlify(xor)): #Saves us from skimming through ugly lines
				
				print >>f, "XOR AGAINST "+str(hex(i))+": " + binascii.unhexlify(xor) #outputs to file. Comfier.
	
f.close()

#SOLUCION:
#XOR AGAINST 0x58: Cooking MC's like a pound of bacon
