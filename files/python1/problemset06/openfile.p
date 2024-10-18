#!/usr/bin/env python3

with open("Python_06.txt", "r") as file_object, open("Python_06_uc.txt", "w") as file_write:
  for line in file_object:
    line = line.rstrip()
    a = (line.upper())
    b =  print(a)
    b
    file_write.write(a) 
