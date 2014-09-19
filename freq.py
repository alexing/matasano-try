#!/usr/bin/python

import os
import string
rootdir = 'txts'
frequencies = {}

def letterOccurrances(aString): 
    for character in aString:
        character=character.lower()
        if character in string.printable:
            if character not in frequencies.keys():
                frequencies[character]=0
            frequencies[character] += 1
    return

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        #print os.path.join(subdir, file)

        f=open(os.path.join(subdir, file))
        letterOccurrances(f.read())
        #print frequencies.keys()
        f.close()

freq=sorted(frequencies.iteritems(),key=lambda tup: tup[1],reverse=True)
print freq
