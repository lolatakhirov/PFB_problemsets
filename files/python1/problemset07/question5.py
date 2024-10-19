#!/usr/bin/env python3
import re 

genes = {}
with open("Python_07.fasta", "r") as fasta_read:
  for line in fasta_read:
    line = line.rstrip()
     if re.search(r"(^>\S*)", list):
       print(list)
    #  genes[gene_list] = ""
   # else:
     # genes[gene_list] += line

#print(genes)

#for match in re.finditer(r"(^>\S*)(.*)", line):
 #     print("id:", match.group(1))
  #    print("desc:", match.group(2))
