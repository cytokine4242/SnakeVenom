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
            m = re.search(':', accession)
            if m:
                accession = None
            else:
                
                accession = "Nana" + accession[9:]
                print(accession)

            #print(accession)
        if (species == 'BOACO'):
            m = re.search(':', accession)
            if m:
                accession = None

            #print(accession)
            
    else:
        accession = None
    #print(accession)
    return accession 


print(sys.argv[1])
GeneFiles = sys.argv[1]
out = sys.argv[2]
specCode = sys.argv[3]
genes = {}
previousGene = ""
with open(GeneFiles) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        if (row[0][0] == "#"):
            continue
        #print(row[8])
        #print(row[2])
        if row[2] == "gene":
            #print(row[2])
            previousGene = [row[0],row[3],row[4],row[6],row[8]]
        accession = AccessionSearch(specCode, row[8])
        if accession is None:
           continue
        else:
            genes[accession] = previousGene
        
with open(out, 'w') as csv_file:  
    writer = csv.writer(csv_file)
    for key, value in genes.items():
       writer.writerow([key, value[0],value[1],value[2],value[3],value[4]])

#print(genes)