#!/usr/bin/env python
from cryp import PKCS7

if PKCS7("YELLOW SUBMARINE",20)=="YELLOW SUBMARINE\x04\x04\x04\x04":
	print "'MIGO 'MIGO 'MIGO 'MIGOOOOO"
