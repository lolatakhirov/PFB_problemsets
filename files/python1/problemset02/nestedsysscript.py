#!/usr/bin/env python3
import sys
count  = int(sys.argv[1])
 
if count <0:
  print("negative")

elif count == 0:
  print("equal")

elif count >50:
  print("greater than 50")

elif count % 3 == 0:
  print("divisible by 3")

elif count <50 and count >0:
  print("smaller than 50 and positive")

  if count % 2 == 0:
    print("it is an even number that is smaller than 50")

