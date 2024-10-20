#!/usr/bin/env python3
import sys 
import re 

dna = sys.argv[1]

def GCcontent(dna):
    length_dna = len(dna)
    G_nucleotides = len(re.findall(r"G", dna))
    C_nucleotides = len(re.findall(r"C", dna))
    final = ((G_nucleotides+C_nucleotides)/(length_dna))*100
    return final
print(GCcontent(dna))
