#!/usr/bin/env python
from __future__ import division
import cryp


text="a"*256

#Why does it not work whit a normal text?
#text="SAMPLE history, a mnemonic acronym for questions medical first responders should ask\nProduct sample, a sample of a consumer product that is given to the consumer so that he or she may try a product before committing to a purchase\nSampling (music), re-using portions of sound recordings in a piece"

#We set a big enough sample, 20000 is ok
tries=20000
iECB=0 #ECB counter
iCBC=0 #CBC counter
for i in range(0,tries):
	mode = cryp.detectAESMode(cryp.encryptionOracle(text))
	if mode == 'ECB': iECB += 1
        elif mode == 'CBC': iCBC += 1
if abs(1-float(iECB/iCBC)<0.05): #Maximum error
	#ECB and CBC counters should be very alike with a p of 0.5.
	#BUT its statiscally ver complicated that they are equal (and if they don't, it
	#doesn't mean the oracle doesn't work)

	print "Anda chill el oracle"
	print "iECB: %d" %iECB
	print "iCBC: %d" %iCBC
else: 
	print "Aqui hay gato encerrado"
	print "iECB: %d" %iECB
	print "iCBC: %d" %iCBC
