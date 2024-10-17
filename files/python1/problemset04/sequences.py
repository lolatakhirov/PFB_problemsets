#!/usr/bin/env python3

list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for item in list:
 # cat(print(len(item), sep = '\n'), print(item, sep = '\n'))
  print(list.index(item), len(item), item)
