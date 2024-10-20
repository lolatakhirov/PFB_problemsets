#!/usr/bin/env python3
import re

#nucleotides{}
genes = {}
nucleotides = {}
#count = 0 
with open("Python_08.fasta", "r") as fasta_read:
  for line in fasta_read:
    line = line.rstrip()
   # print(line)
   # count += 1 
   # if count == 100:
    #  break
    if line.startswith(">"):
      gene_list = line.lstrip(">")
      genes[gene_list] = ""
    else:
      genes[gene_list] += line

    # if match in re.iter(r"ATGC", genes):
     #  nucleotides[gene_list] = ""
    # else:
     # nucleotides[genes] += ....

for item :
  idict = {}
  #print(genes)
  #for gene in genes:
    lola = genes[gene_list]
      #print(lola)

    key_list = list(lola)
    lola2 = len(key_list)
    #lola3 = re.findall(r"[A]", key_list)
    #print(lola3)

dict[lola] = ("A", "C", "G", "T")
print(dict)

    #value_list = list("A", "C", "G", "T")
  



    
#genes[1]["A"]
#found = re.findall(r"A", lola)
#print(len(found))

#header = re.findall(r">", line) 
#sequence = re.findall(r"[AGTC]*", line)

#print(header)
#print(sequence) 

