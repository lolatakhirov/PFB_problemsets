#!/usr/bin/env python3
import Bio
from Bio import SeqIO 
import statistics

#id_dict = SeqIO.to_dict(SeqIO.parse("Python_08.fasta", "fasta"))
#print(id_dict)
#lola = id_dict[]
#print(lola)
new_list = []
new_list2 = []
for seq_record in SeqIO.parse("Python_08.fasta", "fasta"):
#get the sequence information     
    name = (seq_record.id)
    print("id", name)
    lola = (seq_record.seq)
    print("sequence", lola)
    Gcount = (seq_record.count("G"))
    Ccount = (seq_record.count("C"))
    total_GCcount = Gcount+Ccount
    new_list2.append(total_GCcount)
    #print(total_GCcount)
    #print(lola, Gcount)
    #print(lola,Ccount)
    #print(lola)
#count the number of nucleotides per sequence  
    total_nucleotides_per_sequence = (len(lola))
    print("Total_nucleotides", total_nucleotides_per_sequence)
    #print(total_nucleotides_per_sequence)
    #panda = str(total_nucleotides_per_sequence)
    #print(type(panda))

    #panda3 = panda.split()
    #print(panda3)
    new_list.append(total_nucleotides_per_sequence)
longest_sequence = max(new_list)
shortest_sequence = min(new_list)
avg_seq = statistics.mean(new_list)
totalGC_highest = max(new_list2)
totalGC_lowest = min(new_list2) 
avg_GC = statistics.mean(new_list2)
total_sequences = len(new_list)
print("longest seqeuence", longest_sequence)
print("shortest sequence", shortest_sequence)
print("max GC content", totalGC_highest)
print("min GC content", totalGC_lowest)
print("average sequence", avg_seq)
print("average GC", avg_GC)
print("total # sequences", total_sequences)
    

#print(f' name: {name}, total number of nucleotides: {total_nucleotides_per_sequence}, shortest len: {shortest_sequence}, longest len: {longest_sequence} )




    #panda3 = panda2.sort()
    #panda3 = panda.sort
#print(panda2) 
    #split = total_nucleotides_per_sequence.split("")
    #print(total_nucleotides_per_sequence)

#turn the FASTA file into a dictionary 
   #id_dict = SeqIO.to_dict()
   
   
   # Gcount = (seq_record.count("G"))
   # Ccount = (seq_record.count("C"))
   # lola2 = ("total_count", Gcount + Ccount)
   # print(panda2)
   # print(lola2)
   # GC_content = ("GC_content", (Gcount+Ccount)/lola)
   # print(Gcount)
   # print(Ccount)


    #print("count", len(seq_record.count(lola)))
    #print("description", seq_record.description)
    #print("#_nucleotides", len(seq_record.seq))


    
    
    
    


