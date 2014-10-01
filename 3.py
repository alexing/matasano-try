#!/usr/bin/env python
import binascii
import string
from cryp import hexToBin, extendIntInBin, XOR, mostPossibleCharacters
from collections import Counter

encoded="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
encodedBin=hexToBin(encoded)

#What's the most repeated byte in the encoded string?
myCounter=Counter(encodedBin[i:i+8] for i in range(0,len(encodedBin),8))
mostRepeatedChar=myCounter.most_common()[0][0]

#C=p*k
#Got C, we know possible P's... so let's find possible K's
for i in mostPossibleCharacters:
	possibleKey=int(binascii.hexlify(i), 16)^int(mostRepeatedChar,2)
	auxString=extendIntInBin(possibleKey,len(encodedBin))
	xor=XOR(auxString,encodedBin,2)
	if all(char in string.printable for char in binascii.unhexlify(xor)):
		print "XOR AGAINST "+str(hex(possibleKey))+": " + binascii.unhexlify(xor)

#SOLUTION:
#XOR AGAINST 0x58: Cooking MC's like a pound of bacon
