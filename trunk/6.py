#!/usr/bin/env python
from __future__ import division
import base64
import binascii
import string


def stringToBin(string):
	return int(''.join(format(ord(c), '08b') for c in string),2)

def hammingDistance(x,y):
    "Calculate the Hamming distance between two bit strings"
    assert len(x) == len(y)
    x=stringToBin(x)
    y=stringToBin(y)
    count=0
    z=x^y
    while z:
        count += 1
        z &= z-1
    return count

assert hammingDistance("this is a test","wokka wokka!!!")==37
keySizes=[]


f = open('6.txt')
lines = f.read() #FILE TO VARIABLE
f.close()


f=open("out.txt","w+")


lines=(base64.b64decode(lines)).encode("hex")
f.write(lines)

bestScore=1000 #digamos
for keySize in xrange(2,40):

    #distancias
    dAB=hammingDistance(lines[0:keySize],lines[keySize:keySize*2])
    dAC=hammingDistance(lines[0:keySize],lines[keySize*2:keySize*3])
    dAD=hammingDistance(lines[0:keySize],lines[keySize*3:keySize*4])
    dBC=hammingDistance(lines[keySize:keySize*2],lines[keySize*2:keySize*3])
    dBD=hammingDistance(lines[keySize:keySize*2],lines[keySize*3:keySize*4])
    dCD=hammingDistance(lines[keySize*2:keySize*3],lines[keySize*3:keySize*4])
    
    #promedios
    aAB=dAB/keySize
    aAC=dAC/keySize
    aAD=dAD/keySize
    aBC=dBC/keySize
    aBD=dBD/keySize
    aCD=dCD/keySize
    #puntajes
    score=(aAB+aAC+aAD+aBC+aBD+aCD)/6

    if score<bestScore:
        bestScore=score
        bestKeySize=keySize

#print str(bestKeySize)+": "+ str(bestScore)

blocks=[]
for i in xrange(0, len(lines), bestKeySize):
       
    blocks.append(lines[i:i+bestKeySize])
    #print lines[i:i+bestKeySize]

f.close()