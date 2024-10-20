#!/usr/bin/env python3
import sys 
import re 

dna = sys.argv[1]

def first60nucleotides(dna):
    lola4 ="".join(dna.split())
    lola = [lola4[i:i+60] for i in range(0, len(lola4), 60)]
    lola2 =("\n".join(lola))
    return (lola2)
print(first60nucleotides(dna))


