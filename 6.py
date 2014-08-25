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
f.close()