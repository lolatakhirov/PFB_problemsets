#!/usr/bin/env python3 
list = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]
list_iteration = iter(list)
list2 = []
list3 = []

for lister1 in list_iteration :
  if lister1 % 2 == 0:
   list2.append(lister1)
  if lister1 % 2 == 1:
    list3.append(lister1)
b = sum(list3)
a = sum(list2)

print(b)
print(f' Sum of even numbers: {a} and sum of odds: {b}')
