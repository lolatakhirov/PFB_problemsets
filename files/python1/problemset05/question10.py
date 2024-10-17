#!/usr/bin/env python3
import sys

#lola_dictionary= {"book" : "Hunger Games", "song" : "Quinn XCII", "tree" : "maple", "organism" : "fly"}

fav_thing = sys.argv[1]
fav_value = sys.argv[2]
lola_dict = {fav_thing : fav_value}

print(lola_dict[fav_thing])
