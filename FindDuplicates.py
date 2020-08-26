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
dedup_records = defaultdict(list)
for record in SeqIO.parse(inFast, "fasta"):
    # Use the sequence as the key and then have a list of id's as the value
    try:
        a[0]= dedup_records[str(record.seq)]
        a[1]= record.id
        duplicates.append(a)
    except:
        dedup_records[str(record.seq)].append(record.id)



print(duplicates)