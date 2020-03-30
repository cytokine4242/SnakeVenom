
import sys
import csv
from Bio import SeqIO

GeneFile = sys.argv[1]
RNAFile = sys.argv[2]
CDSFile = sys.argv[3]
fasta = sys.argv[4]
print(GeneFile)
print(RNAFile)
print(CDSFile)
print(fasta)

genes = {}

with open(GeneFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        
        genes[row[0]] = [row[1],row[2],row[3]]    


cds = {}
with open(CDSFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cds[row[2]] = [row[0]]    
        #print(row)

print(cds['XP_026552168.1'])

rnaDict = {}
with open(RNAFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        rnaDict[row[0]] = [row[1]]    
        #print(row)

print(rnaDict['rna5937'])



addedGenes = []
KeepRecords = []
with open(fasta, "r") as handle:
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
        #print(accession)
        found = False
        try:

            
            rna = cds[accession][0]
            #print(accession, " is in cds dict" , cds[accession],rna)
            found = True
                
            gene = rnaDict[rna][0]
            #print(accession, "is in Gene dict")
            #print(gene)
            if gene in addedGenes:
                print("gene already present")
            else:
                addedGenes.append(gene)
                KeepRecords.append(record)
                print("added" , record.name , "to fasta" )

        except:
            #print(accession, "not found in GFF")
            a=1

SeqIO.write(KeepRecords, fasta + ".duplicateRemoved.fas" , "fasta")
