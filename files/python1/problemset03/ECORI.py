#!/usr/bin/env python3
import sys 

#EcoRI site is GAATTC

A = (sys.argv[1].find("GAATTC"))
B = (A+5)

print(f' EcoRI startPos: {A} endPos: {B}.')
