#!/usr/bin/env python
#
#Standarized conversion library and other tools repeating throughout


from __future__ import division
import base64
import binascii
import sys
from nltk import wordpunct_tokenize
from nltk.corpus import stopwords #### sudo apt-get install python-nltk
from itertools import cycle


mostPossibleCharacters=[' ','e','t','a','o','i','n']

def hexToBase64(hexStr):
	return base64.b64encode(hexStr.decode("hex"))

def base64ToHex(base64Str):
	return base64.b64decode(base64Str)
	#return str(binascii.hexlify(binascii.a2b_base64(base64Str)))

def XOR(buf1,buf2,base):
	if len(buf1) != len(buf2):
		raise Exception("Bufs must be same length %d!=%d" % (len(buf1), len(buf2)) )
	b1=int(buf1, base)
	b2=int(buf2, base)
	
	ret="%x" %(b1^b2)
	if len(ret)%2!=0: #odd number padding
		return "0"+ret
	return ret

def hexToBin(hexStr):
	encodedBin=""
	for c in hexStr:
		encodedBin+=format(int(c,16),'04b')
	return encodedBin

def extendIntInBin(i,len):
	return format(i, '08b')*(len//8)
def repeatToLength(stringToExpand, length):
   return (stringToExpand * ((length//len(stringToExpand))+1))[:length]

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

def bruteForceKeySizes(lines):
	keySizes=[]
	for keySize in range(2,40):

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

	    keySizes.append((keySize,score))
	keySizes.sort(key=lambda tup: tup[1])
	return [item[0] for item in keySizes[:5]]

def breakIntoAndTransposeBlocks(lines,keySize):
	blocks=[]
	tBlocks=[""]*keySize
	for i in range(0,len(lines),keySize):
		block=lines[i:i+keySize]
		aux=0
		for j in block:
			tBlocks[aux]+=j
			aux+=1

	return tBlocks

def getEngProbability(text):
    tokens = wordpunct_tokenize(text)
    words = [word.lower() for word in tokens]

    # Compute per language included in nltk number of unique stopwords appearing in analyzed text
    stopwords_set = set(stopwords.words('english'))
    words_set = set(words)
    common_elements = words_set.intersection(stopwords_set)

    p = len(common_elements) # language "score"
    return p


def encodeRepeatingKeyXOR(plaintext,key):
	binLine=''.join(format(ord(x), '08b') for x in plaintext)
	auxString=''.join(format(ord(x), '08b') for x in key)
	auxString=repeatToLength(auxString,len(binLine))
	return XOR(binLine, auxString,2)

def decodeRepeatingKeyXOR(ciphertext,key):
    binLine=hexToBin(binascii.b2a_hex(ciphertext).decode())
    auxString=''.join(format(ord(x), '08b') for x in key)
    auxString=repeatToLength(auxString,len(binLine))
    return XOR(binLine, auxString,2)

def PKCS7(stringToPad,blockSize):
	remainder=blockSize%len(stringToPad)
	if remainder==0:
		return stringToPad
	return stringToPad+chr(remainder)*remainder
	