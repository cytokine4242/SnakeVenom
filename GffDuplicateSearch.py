
import sys
import csv
from Bio import SeqIO
from Bio.SeqIO import FastaIO
#load in handles
GeneFile = sys.argv[1]
RNAFile = sys.argv[2]
CDSFile = sys.argv[3]
fasta = sys.argv[4]
out = sys.argv[5]
print(GeneFile)
print(RNAFile)
print(CDSFile)
print(fasta)

genes = {}
#read genes
with open(GeneFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        
        genes[row[0]] = [row[1],row[2],row[3]]    


cds = {}
#read cds
with open(CDSFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        cds[row[2]] = [row[0]]    
        #print(row)


rnaDict = {}
#read RNA
with open(RNAFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        rnaDict[row[0]] = [row[1]]    
        #print(row)




addedGenes = []
KeepRecords = []
records = 0
repeats = 0
uniq = 0
#open fasta
with open(fasta, "r") as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        #print(record.name)
        records = records +1
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
        #lookup if gene is already used 
        try:

            
            rna = cds[accession][0]
            #print(accession, " is in cds dict" , cds[accession],rna)
            found = True
                
            gene = rnaDict[rna][0]
            #print(accession, "is in Gene dict")
            #print(gene)
            if gene in addedGenes:
                print("removed", record.name, "gene already present")
                repeats = repeats +1
            else:
                addedGenes.append(gene)
                KeepRecords.append(record)
                print("added" , record.name , "to fasta" )
                uniq = uniq +1
        except:
            #print(accession, "not found in GF
            KeepRecords.append(record)
            print("added" , record.name , "to fasta" )
            uniq = uniq +1 


#write out uniqe files
with open(out, "w") as output_handle:
	fasta_out = FastaIO.FastaWriter(output_handle, wrap=None)
	fasta_out.write_file(KeepRecords)
#print log info
print(" Number of records = ", records)
print("Number of uniq = ", uniq )
print("number of removed = ", repeats)
