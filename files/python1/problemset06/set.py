#!/usr/bin/env python3

collection1 = (3, 14, 15, 9, 26, 5, 35, 9)
collection2 = (60, 22, 14, 0, 9, "g")

a = set(collection1) 
b = set(collection2) 


c = (a-b)
d = (a | b)
e = (a & b) 
f = (a ^ b)

print(f' The difference is {c} the union is {d} the intersection is {e} and the symmetrical difference is {f}')
