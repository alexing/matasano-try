#!/usr/bin/env python
import binascii
from cryp import XOR,repeatToLength

key="ICE"
stanza="Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
solution="0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
#Had a problem here with the end-of-line of the solution. 
#Solved it like it was all in the same line.

binLine=''.join(format(ord(x), '08b') for x in stanza)
auxString=''.join(format(ord(x), '08b') for x in key)
auxString=repeatToLength(auxString,len(binLine))
	
if XOR(binLine, auxString,2) == solution:
	print "BIEM PIOLAAh"

