#!/usr/bin/env python
from cryp import XOR


buf1="1c0111001f010100061a024b53535009181c"
buf2="686974207468652062756c6c277320657965"
buf3="746865206b696420646f6e277420706c6179"

if XOR(buf1,buf2,16)==buf3:
	print "GUENA, GUACHIIIIIN"
	#print " "
	#print "And bufs said: "
	#print buf2.decode("hex")
	#print buf3.decode("hex")