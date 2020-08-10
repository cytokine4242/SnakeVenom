import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 
import operator

genes = sys.argv[1]
out = sys.argv[2]
unsort =[]
with open(genes) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        unsort.append(row)
    
    
    
    
    sort = sorted(unsort,key=lambda x: (x[1],int(x[2])))


with open(out, 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for line in sort:
       writer.writerow(line)
