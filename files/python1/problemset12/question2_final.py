#!/usr/bin/env python3
import Bio
from Bio import SeqIO 

id_dict = SeqIO.to_dict(SeqIO.parse("Python_08.fasta", "fasta"))
#print(id_dict)

for id_ in id_dict:
    seq = id_dict[id_]
    twice = id_dict[id_][0]
    #print(seq)
    print(twice)