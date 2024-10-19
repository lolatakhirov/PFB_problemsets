#!/usr/bin/env python3
import re

with open("Python_07_ApoI.fasta", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    found = re.sub(r"([AG])(AATT[CT])", r"\1^\2", line)
    print(found)




