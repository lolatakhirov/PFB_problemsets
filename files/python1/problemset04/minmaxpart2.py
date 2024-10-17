#!/usr/bin/env python3
import sys

minval = int(sys.argv[1])
maxval = int(sys.argv[2])
for value in range(minval, maxval):
 print(minval)
 print(maxval)

lola = []

for value in range(minval, maxval):
  if value %2 == 1: 
    lola.append(value)

print(lola)
