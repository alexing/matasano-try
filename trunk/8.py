#!/usr/bin/env python
import cryp
from Crypto.Cipher import AES

f = open('8.txt')
lines = f.readlines() #FILE TO LIST
f.close()

for i, line in enumerate(lines):
	#Each byte is two chars (hex-encoded)... so 32
	chunks = [line[j:j+32] for j in range(0, len(line), 32)]
	repeated=len(chunks) - len(set(chunks)) #"Set" type groups duplicates, making them easy to spot

	if repeated>0:
		print "Line %d has probable block cipher (%d repeated blocks)" %(i, repeated)