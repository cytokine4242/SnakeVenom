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
dedup_records = {}
for record in SeqIO.parse(inFast, "fasta"):
    # Use the sequence as the key and then have a list of id's as the value
    a = record.name
    print(a)

with open(outFast, 'w') as output:
    for item in duplicates:
        # Join the ids and write them out as the fasta
        output.write('%s\n' % item)

print(duplicates)
