#!/usr/bin/env python3
import re

genes= {}
with open("Python_07_ApoI.fasta", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    found = re.sub(r"([AG])(AATT[CT])", r"\1^\2", line)
    if line.startswith(">"):
      gene_list = found.lstrip(">")
      genes[gene_list] = ""
    else:
      genes[gene_list] += found

sequence = genes[gene_list]   
lola = sequence.split("^")
lola2 = sorted(lola, key = len)
print(lola2)





#for match in re.findall(r"(\^.*)", found):
 #    print(match)
     # print(len(lola))
