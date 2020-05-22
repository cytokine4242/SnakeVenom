import sys
import csv
from Bio import SeqIO
from Bio.SeqIO import FastaIO

GeneFile = sys.argv[1]
fasta = sys.argv[2]
specCode = sys.argv[3]

scaffolds = {}
accession = []
records = 0
speciesAccession =[]
with open(fasta, "r") as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        #print(record.name)
        records = records +1
        ID = record.name.split(" ")
        db = ID[0].split('_')[0]
        spec = ID[0].split('_')[1]
        accessionList = ID[0].split('_')
        
        if (spec == specCode):
            size =len(accessionList)
            accession = ""
            for i in range(3,size):
                accession = accession + accessionList[i] + "_"
            accession = accession[:-1]
            speciesAccession.append(accession)
            print(ID,accession)
            

print(len(speciesAccession))
accToScaffolds = {}
with open(GeneFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if (row[0][0] == "#"):
            continue
        #print(row[8])
        protein = row[8].split("=")
        accession=protein[-1]
        #print(accession)
        accToScaffolds[accession] = row[0]
scaffoldCount = {}
for acc in speciesAccession:
    try:
        scaffoldCount[accToScaffolds[acc]] += 1
    except: 
        scaffoldCount[accToScaffolds[acc]] = 1
    print(acc, 'in', accToScaffolds[acc])


print(scaffoldCount)