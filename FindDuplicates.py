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
#read in the files 
for record in SeqIO.parse(inFast, "fasta"):
    # Use the sequence as the key and then have a list of id's as the valuei
    #print(record.id)
    print(len(dedup_records))
    try:
        a =[]
        #check if sequence already exists 
        b = dedup_records[str(record.seq)]
        a.append(dedup_records[str(record.seq)])
        a.append(record.id)
        print(record.id)
        #if it doesnt add it 
        duplicates.append(a)
    except KeyError:
        #remove but keep track of duplicates
        dedup_records[str(record.seq)]= record.id
        print(record.id)
#Write out duplicates
with open(outFast, 'w') as output:
    for item in duplicates:
        # Join the ids and write them out as the fasta
        output.write('%s\n' % item)

print(duplicates)
