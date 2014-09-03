#!/usr/bin/env python
#
#Standarized conversion library and other tools repeating throughout


from __future__ import division
import base64
import binascii

def hexToBase64(hexStr):
	return base64.b64encode(hexStr.decode("hex"))

def base64ToBytes(base64Str):
	return (base64.b64decode(base64Str))

def XOR(buf1,buf2,base):
	if len(buf1) != len(buf2):
		raise Exception("Bufs must be same length")
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

	    keySizes.append((keySize,score))
	keySizes.sort(key=lambda tup: tup[1])
	return [item[0] for item in keySizes[:5]]

def bruteForceXOR(bytes):
	best = (0.0, None, None)
    for keyBytes in range(0, 255):
        try:
            text = bytes([b1 ^ b2 for b1, b2 in zip(bytes, cycle(keyBytes))]).decode()
            score = ##CALCULAR PROBA
            if score > best[0]:
                best = (score, keyBytes, text)
        except UnicodeDecodeError:
            pass
    return best[1:]


def breakIntoAndTransposeBlocks(lines,keySize):
	blocks=[""]*keySize #Break the code into blocks
	for i, byte in enumerate(lines):
		blocks[i % keySize] += byte
	return blocks

#def breakIntoBlocks(lines,keySize):
#	blocks=[] #Break the code into blocks
#	for i in xrange(0, len(lines), keySize):
#		blocks.append(lines[i:i+keySize])
#	return blocks
#def transposeBlocks(blocks,keySize):
#	transposedBlocks=[] #transpose them
#	for i in xrange(0,keySize):
#		word=""
#		for j in blocks:
#			word+=j[i]
#		transposedBlocks.append(word)