#!/usr/bin/env python3
import re 

with open("Python_07.fasta", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
   
    for match in re.finditer(r"(^>\S*)(.*)", line):
      print("id:", match.group(1))
      print("desc:", match.group(2))



# for (id, desc) in re.search(r"(^>\S*.*)([ATGC*])", line):
 #   print("id:", id)
  #  print("des:", desc)
