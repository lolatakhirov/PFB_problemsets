#!/usr/bin/env python3
import sys 
import re 

dna = sys.argv[1]

def revcomp(dna):
    lola= dna[::-1]
    return lola
print(revcomp(dna))

