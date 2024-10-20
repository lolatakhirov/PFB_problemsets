#!/usr/bin/env python3
import sys 
import re 

#count = 60
dna = sys.argv[1]

def first60nucleotides(dna):
    lola = [dna[i:i+60] for i in range(0, len(dna), 60)]
       #lola = dna.append("\n",count )
       #count = count + 60 
    lola2 =("\n".join(lola))
    return (lola2)
print(first60nucleotides(dna))
 
       # lola = item[count]
       # count = count + 60
#print(dna[0:60])  

#print(first60nucleotides(dna))


