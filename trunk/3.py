#!/usr/bin/env python
import binascii
import string

encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
encodedBin=""
decoded=""
f=open("out.txt","w+")
for c in encoded:
		encodedBin+=format(int(c,16),'04b')


for i in xrange(0x00,0xFF):
	auxString=format(i, '08b')*(len(encodedBin)/8)
	b1=int(auxString, 2)
	b2=int(encodedBin, 2)

	
	xor="%x" %(b1^b2)
	if len(xor)%2==0: #Not nice but works. Some lines don't have an odd number of characters and script implodes. 
			if all(char in string.printable for char in binascii.unhexlify(xor)): #Saves us from skimming through ugly lines
				
				print >>f, "XOR AGAINST "+str(hex(i))+": " + binascii.unhexlify(xor) #outputs to file. Comfier.
	


f.close()

#SOLUCION:
#XOR AGAINST 0x58: Cooking MC's like a pound of bacon
