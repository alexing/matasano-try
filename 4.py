#!/usr/bin/env python
import binascii
import string
from cryp import hexToBin, extendIntInBin, XOR,getEngProbability,mostPossibleCharacters
from collections import Counter

f = open('4.txt')
lines = f.readlines() #FILE TO LIST
f.close()


lineCounter=0
plainTexts=[]
bestScore=0


for line in lines:
	lineCounter+=1
	encoded=line.rstrip('\n') #CHOMP
	encodedBin=hexToBin(encoded)
	
	#What's the most repeated byte in the encoded string?
	myCounter=Counter(encodedBin[i:i+8] for i in range(0,len(encodedBin),8))
	mostRepeatedChar=myCounter.most_common()[0][0]

	for i in mostPossibleCharacters:
		possibleKey=int(binascii.hexlify(i), 16)^int(mostRepeatedChar,2)
		auxString=extendIntInBin(possibleKey,len(encodedBin))
		xor=XOR(auxString,encodedBin,2)
		if all(char in string.printable for char in binascii.unhexlify(xor)): #Saves us from skimming through ugly lines
			plainTexts.append((str(lineCounter),str(hex(possibleKey)),binascii.unhexlify(xor))) #outputs to file. Comfier.

for option in plainTexts:
	p=getEngProbability(option[2])
	if p>bestScore:
		bestScore=p
		plainText=option
print "LINE "+ plainText[0]+ ") XOR AGAINST "+plainText[1]+": " + plainText[2]


#SOLUTION: 
#Line 171) XOR AGAINST 0x35: Now that the party is jumping