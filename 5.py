#!/usr/bin/env python
import binascii

key="ICE"
stanza="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
solution="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
#Had a problem here with the end-of-line of the solution. 
#Solved it like it was all in the same line.


def repeatToLength(stringToExpand, length):
   return (stringToExpand * ((length/len(stringToExpand))+1))[:length]

def XOR(buf1,buf2):
	if len(buf1) != len(buf2):
		raise Exception("Bufs must be same length")
	b1=int(buf1, 2)
	b2=int(buf2, 2)
	
	ret="%x" %(b1^b2)
	if len(ret)%2!=0: #odd number padding
		return "0"+ret
	return ret

binLine=''.join(format(ord(x), '08b') for x in stanza)
auxString=''.join(format(ord(x), '08b') for x in key)
auxString=repeatToLength(auxString,len(binLine))
	
if XOR(binLine, auxString) == solution:
	print "BIEM PIOLAAh"

