

import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 



inFast = sys.argv[1]
outFast = sys.argv[2]

speciesAccession =[]
NAJNAcheck ={}
HYDUCRcheck = {}

outputrecord =[]
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

with open(outFast, "w") as output_handle:
    SeqIO.write(outputrecord, output_handle, "fasta")