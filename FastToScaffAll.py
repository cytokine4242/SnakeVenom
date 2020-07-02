import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO

def AccessionSearch(species, search):

    if species == 'NOTSC' or species == 'PSETE':
        m = re.search('protein_id=(.*)', search)
        #print("Transcript", m)
    elif (species == 'BOACO'):
        m = re.search('ID=(.*)', search)
        
    elif (species == 'CROVV'):
        m = re.search('Crovir_Transcript_ID=(.*)', search)
    elif (species == 'NAJNA'):
        m = re.search('ID=(.*)', search)


        #ID=Naja_naja35841-RA
    elif ( species == 'HYDCUR'):
        m = re.search('Parent=(.*)', search)

    if m:
        match = m.group(1)
        accession = match.split(";")
        accession = accession[0]
        if (species == 'CROVV'):
            name = accession.split("-")
            accession = name[0] + "-protein-" + name[2]
            #print("FOUND",accession)
        if (species == 'NAJNA'):
            accession = "Nana" + accession[9:]
            #print(accession)
            
    else:
        accession = None
    
    return accession 

GeneFile = sys.argv[1]
fasta = sys.argv[2]
specCode = sys.argv[3]
print(specCode)
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
            #print(ID,accession)
            

print(len(speciesAccession))
accToScaffolds = {}
with open(GeneFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if (row[0][0] == "#"):
            continue
        #print(row)
        try:
            a =(row[8])
        except: 
            print(row)
        accession = AccessionSearch(specCode, row[8])
        if accession is None:
           continue
        #protein = row[8].split("=")
        #accession=protein[-1]
        #print(accession)
        accToScaffolds[accession] = row[0]
        #print(accession)
scaffoldCount = {}
for acc in speciesAccession:
    #print(acc)
    try:
        
        scaffoldCount[accToScaffolds[acc]] += 1
        print(acc, 'in', accToScaffolds[acc])
    except: 
        #print(accToScaffolds[acc])
        try:
            scaffoldCount[accToScaffolds[acc]] = 1
            print(acc, 'in', accToScaffolds[acc])   
        except:
            print("couldtn find accession",acc)
    #print(acc, 'in', accToScaffolds[acc])
    

print(scaffoldCount)





