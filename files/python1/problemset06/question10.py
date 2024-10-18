#!/usr/bin/env python3

with open("ferret_all_genes.tsv", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    all_genes = set(line) 
    print(all_genes)
