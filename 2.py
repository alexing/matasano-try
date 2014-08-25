#!/usr/bin/env python

buf1="1c0111001f010100061a024b53535009181c"
buf2="686974207468652062756c6c277320657965"
buf3="746865206b696420646f6e277420706c6179"

def XOR(buf1,buf2):
	if len(buf1) != len(buf2):
		raise Exception("Bufs must be same length")
	b1=int(buf1, 16)
	b2=int(buf2, 16)
		
	return "%x" %(b1^b2)

if XOR(buf1,buf2)==buf3:
	print "GUENA, GUACHIIIIIN"
	#print " "
	#print "And bufs said: "
	#print buf2.decode("hex")
	#print buf3.decode("hex")