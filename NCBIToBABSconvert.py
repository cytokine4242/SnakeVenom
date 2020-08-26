import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO


fasta = sys.argv[1]
mapping = sys.argv[2]
out =  sys.argv[3]


MapDict = {}
with open(mapping) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        MapDict[row[0]] = row[1]
recordNum =0 
with open(fasta) as original, open(out, 'w') as corrected:
    for record in SeqIO.parse(original, "fasta"):
        #print(record.name)
        recordNum = recordNum +1
        ID = record.name.split(" ")
        db = ID[0].split('_')[0]
        spec = ID[0].split('_')[1]
        accession = ID[0].split('_')[3] + "_" + ID[0].split('_')[4]
        #print(record.id)
        #print(accession)
        #print(MapDict[accession])
        record.id = MapDict[accession]
        #print(record.id)
                     # prints 'bar' as expected
        print(recordNum)
        SeqIO.write(record, corrected, 'fasta')
