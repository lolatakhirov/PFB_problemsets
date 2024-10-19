#!/usr/bin/env python3
import re

#count = 0 

enzymes = {}
with open("bionet 2.txt", "r") as fasta_read:
:w

  for line in fasta_read:
    line = line.rstrip()
   # print(line)
   #count += 1
   # if count == 11:
     # break

    something =  re.split(r"\s{2,}", line)
    enzymes[something[0]] = something[1]
  print(enzymes)
      


  


