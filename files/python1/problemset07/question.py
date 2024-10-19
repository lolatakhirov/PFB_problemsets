#!/usr/bin/env python3
import re
with open("Python_07_nobody.txt", "r") as seq_read:
  for line in seq_read:
    line = line.rstrip()
    found = re.search(r"Nobody", line)
    sub = re.sub(r"Nobody", "Lola", line)
    print(sub)
