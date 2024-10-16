#!/usr/bin/env python3
import sys 

a = sys.argv[1].replace("A", "t")
b = a.replace("T", "a")
c = b.replace("C", "g")
d = c.replace("G", "c")
e = d.upper()
print(e[::-1])
