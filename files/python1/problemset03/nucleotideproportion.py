#!/usr/bin/env python3
import sys 
A_count = sys.argv[1].count("A")
a_count = sys.argv[1].count("a")
A_count_total = A_count+a_count
T_count = sys.argv[1].count("T")
t_count = sys.argv[1].count("t")
T_count_total = T_count+t_count
ATproportion= A_count_total + T_count_total 
total = len(sys.argv[1])
print(ATproportion/total)


C_count = sys.argv[1].count("C")
c_count = sys.argv[1].count("c")
C_count_total = C_count+c_count
G_count = sys.argv[1].count("G")
g_count = sys.argv[1].count("g")
G_count_total = G_count+g_count
GCproportion= G_count_total + C_count_total
print(GCproportion/total)
