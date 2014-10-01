#!/usr/bin/env python
import cryp
import binascii
import string
from collections import Counter

assert cryp.hammingDistance("this is a test","wokka wokka!!!")==37

f = open('6.txt')
lines = f.read() #FILE TO VARIABLE
f.close()

lines=cryp.base64ToHex(lines)
keySizes=cryp.bruteForceKeySizes(lines)
keyCandidates=[]
for keySize in keySizes:
    blocks=cryp.breakIntoAndTransposeBlocks(lines,keySize)

    possibleKeys={}
    for char in cryp.mostPossibleCharacters:
        possibleKeys[char]=""

    for block in blocks:
        encodedBin=cryp.hexToBin(block.encode('hex'))#!!!!!!!!!!!!!!!!!!!!

        #What's the most repeated byte in the encoded string?
        myCounter=Counter(encodedBin[i:i+8] for i in range(0,len(encodedBin),8))
        mostRepeatedChar=myCounter.most_common()[0][0]
        
        #C=p*k
        #Got C, we know possible P's... so let's find possible K's
        for i in cryp.mostPossibleCharacters:
            possibleKeyChar=int(binascii.hexlify(i), 16)^int(mostRepeatedChar,2)
            auxString=cryp.extendIntInBin(possibleKeyChar,len(encodedBin))
            xor=cryp.XOR(auxString,encodedBin,2)
            if all(char in string.printable for char in binascii.unhexlify(xor)):
                #Each possible character may trigger the key, we store them
                #in a dictionary structure so they don't mix
                possibleKeys[i]+=chr(possibleKeyChar)

    #Now let's check which is the right one        
    key=""
    for possibleKey in possibleKeys:
        if len(possibleKeys[possibleKey])==keySize:
            
            key=possibleKeys[possibleKey] #this one
            xor=cryp.decodeRepeatingKeyXOR(lines,key) #where the magic happens
            print "KEY: %s \nPLAINTEXT: %s" %(key, xor.decode("hex")) #voila
