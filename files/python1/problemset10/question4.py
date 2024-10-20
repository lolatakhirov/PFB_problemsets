#!/usr/bin/env python3
import sys 
import re 

width = sys.argv[2]

with open(sys.argv[1], "r") as fasta_read:
  for line in fasta_read:
    line = line.rstrip()

def first_nucleotides(dna):
    lola4 ="".join(dna.split())
    lola = [lola4[i:i+int(width)] for i in range(0, len(lola4), int(width))]
    lola2 =("\n".join(lola))
    return (lola2)
print(first_nucleotides(dna))

