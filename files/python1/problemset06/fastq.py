#!/usr/bin/env python3
counts = 0
counts1 = 0
counts2 = 0
with open("Python_06.fastq", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    count_characters = len(line)
    counts += count_characters
    count_lines = len("\n")
    counts1 += count_lines 
    average = (counts/counts1)
    counts2 += average
    
print(counts)
print(counts1)
print(counts2)



