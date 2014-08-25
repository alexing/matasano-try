#!/usr/bin/env python
import base64

string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

stringB64=base64.b64encode(string.decode("hex"))

if stringB64=="SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
	print "ALELUYA HERMANOS"
	#print "And just because, what they made you translate was: \"" + string.decode("hex")+"\""