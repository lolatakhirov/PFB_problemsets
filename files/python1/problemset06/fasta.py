#!/usr/bin/env python3

genes = {}
with open("Python_06.fasta", "r") as fasta_read:
  for line in fasta_read:
    line = line.rstrip()  
    if line.startswith(">"):
      gene_list = line.lstrip(">")
      genes[gene_list] = ""
    else:
      genes[gene_list] += line 

print(genes)
	







