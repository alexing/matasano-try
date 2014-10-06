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
from random import randint,random
import operator
from Crypto.Cipher import AES

mostPossibleCharacters=[' ','e','t','a','o','i','n']

def hexToBase64(hexStr):
	return base64.b64encode(hexStr.decode("hex"))

def base64ToHex(base64Str):
	return base64.standard_b64decode(base64Str)
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

def cryptXOR(plaintext,key):
	return "".join(["%02x" % (ord(p) ^ ord(k)) for (p, k) in zip(plaintext, cycle(key))]).decode("hex")




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


def decodeAES_ECB(ciphertext,key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext=cipher.decrypt(ciphertext)
	return plaintext

def encodeAES_ECB(plaintext,key):
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext=cipher.encrypt(plaintext)
	return ciphertext

def PKCS7(stringToPad,blockSize):
	assert 0 < blockSize < 255, 'blocksize must be between 0 and 255'
  	assert len(stringToPad) > 0 , 'string length should be non-negative'

	remainder = blockSize - (len(stringToPad) % blockSize)
	return stringToPad + (chr(remainder) * remainder)


def unpadPKCS7(stringToUnpad,blockSize):
	padLen = ord(stringToUnpad[-1]) # last byte contains number of padding bytes
	if padLen > blockSize:
		return stringToUnpad
	if padLen > len(stringToUnpad):
		return stringToUnpad
	return stringToUnpad[:-padLen]

def encodeAES_CBC(plaintext,key,iv):
	#Blocksize is assumed to be ==keysize
	assert len(iv)==len(key)
	blockSize=len(key)
	prevBlock=iv
	encoded=""
	for i in range(0,len(plaintext),blockSize):
		block=plaintext[i:i+blockSize]
		if len(block)<blockSize:
			block=PKCS7(block,blockSize)
		cipherBlock=encodeAES_ECB(cryptXOR(block,prevBlock),key)
		encoded+=cipherBlock
		prevBlock=cipherBlock
	return encoded

def decodeAES_CBC(ciphertext,key,iv):
	#Blocksize is assumed to be ==keysize
	assert len(iv)==len(key)
	blockSize=len(key)
	prevBlock=iv
	decoded=""
	for i in range(0, len(ciphertext), blockSize):
		block = ciphertext[i:i+blockSize]
		plainBlock = cryptXOR(decodeAES_ECB(block, key), prevBlock)
		decoded+=plainBlock
		prevBlock = block
	return unpadPKCS7(decoded,blockSize)
	#return decoded

def randomAESKey():
	return reduce(operator.add, ('%c' % randint(0, 255) for i in range(16)))

def encryptionOracle(text):
	#Add random prefix and random suffix, and then pkcs7 pad the resulting string
	prefix=reduce(operator.add, ('%c' % randint(0, 255) for i in range(randint(5, 10))))
	suffix=reduce(operator.add, ('%c' % randint(0, 255) for i in range(randint(5, 10))))
	text=PKCS7(prefix+text+suffix,16)

	#Generate random key and random probability
	key=randomAESKey()
	p=random()
	#P(ECB)=0.5 and P(CBC)=0.5
	if p<0.5: #ECB Mode
		cipher=encodeAES_ECB(text,key)
	else: #CBC Mode
		iv=randomAESKey() #len(iv)==len(key) so we use the same function to randomize the iv
		cipher=encodeAES_CBC(text,key,iv)

	return cipher