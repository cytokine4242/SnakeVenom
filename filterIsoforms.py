
import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 


#set input and output file handles 
inFast = sys.argv[1]
outFast = sys.argv[2]

speciesAccession =[]
NAJNAcheck ={}
HYDUCRcheck = {}
PROFLcheck ={}
outputrecord =[]
#open the read in fasta file and read in HYDCUR, NAJNA, or PROFL entries for filtering isoforms 
with open(inFast, "r") as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        #print(record.name)
        
        ID = record.name.split(" ")
        db = ID[0].split('_')[0]
        spec = ID[0].split('_')[1]
        accessionList = ID[0].split('_')
        
        size =len(accessionList)
        accession = ""
        for i in range(3,size): 
            accession = accession + accessionList[i] + "_"
        accession = accession[:-1]
        speciesAccession.append(accession)

        if spec == "NAJNA":
            
            check = accession.split('-')
            check = check[0]
            try:
                NAJNAcheck[check]
                continue
            except KeyError:
                NAJNAcheck[check] = True
                print(accession)
        if spec == "PROFL":
            check = accession.split('.')
            check = check[0]
            try:
                PROFLcheck[check]
                continue
            except KeyError:
                PROFLcheck[check] = True
                print(accession)


        elif spec == "HYDCUR":
            check = accession.split('.')
            check = check[0]
            try:
                HYDUCRcheck[check]
                continue
            except KeyError:
                HYDUCRcheck[check] = True
                print(accession)
        outputrecord.append(record)

#write it out again without the secondary isoforms 
with open(outFast, "w") as output_handle:
    SeqIO.write(outputrecord, output_handle, "fasta-2line")
