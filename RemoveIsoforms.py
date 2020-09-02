#remove isofroms based on names
import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 
from collections import defaultdict
inFast = sys.argv[1]
outFast = sys.argv[2]

speciesAccession =[]
outputrecord =[]

duplicates = []
dedup_records = []
a= 0
for record in SeqIO.parse(inFast, "fasta"):
    # Use the sequence as the key and then have a list of id's as the value
    b = record.description
    m = re.search('isoform', b)
    if m:
       match = m.string
       print(match)
       m = re.search('isofrom X1', b)
       if m:
           dedup_records.append(record)
       else:
           duplicates.append(record)   
    else:
       dedup_records.append(record)  
    a = record.description



SeqIO.write(duplicates, outFast+"removedIso.fasta", "fasta-2line")
SeqIO.write(dedup_records, outFast+"filteredIso.fasta", "fasta-2line")
print(duplicates)
