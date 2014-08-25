#!/usr/bin/env python
import binascii
import string

f = open('4.txt')
lines = f.readlines() #FILE TO LIST
f.close()


f=open("out.txt","w+")
lineCounter=0

for line in lines:
	lineCounter+=1
	encoded=line.rstrip('\n') #CHOMP
	encodedBin=""
	decoded=""
	for c in encoded:
		encodedBin+=format(int(c,16),'04b')


	for i in xrange(0x00,0xFF):
		auxString=format(i, '08b')*(len(encodedBin)/8)
		b1=int(auxString, 2)
		b2=int(encodedBin, 2)

	
		xor="%x" %(b1^b2)
		if len(xor)%2==0: #Not nice but works. Some lines don't have an odd number of characters and script implodes. 
			if all(char in string.printable for char in binascii.unhexlify(xor)): #Saves us from skimming through ugly lines
				
				print >>f, "Line "+str(lineCounter)+") XOR AGAINST "+str(hex(i))+": " + binascii.unhexlify(xor) #outputs to file. Comfier.
	


f.close()

#SOLUTION: 
#Line 171) XOR AGAINST 0x35: Now that the party is jumping