
#!/usr/bin/env python3

genes = {}
with open("Python_06.seq.txt", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    gene_id, seq = line.split()
    genes[gene_id] = seq[::-1]
    print(genes)
print("This is the reverse complement")
