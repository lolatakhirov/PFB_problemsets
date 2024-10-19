#!/usr/bin/env python3
import re

with open("Python_07_ApoI.fasta", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    founder = re.findall(r"[AG]AATT[CT]", line)
    print(founder)
  



# R = A or G 
#N = any nucleotide 
#Y = C or T 
#Need RAATTY

