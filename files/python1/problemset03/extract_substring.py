#!/usr/bin/env python3
import sys 

hundred = (sys.argv[1][100:201])
G_count = (hundred.count("G"))
g_count = (hundred.count("g"))
print(G_count+g_count)
 
