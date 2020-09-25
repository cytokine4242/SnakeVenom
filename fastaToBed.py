import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 


#funciton to write out a bed file
def writeBed(bed,name):
    with open(name, 'w') as csv_file:  
        writer = csv.writer(csv_file,delimiter='\t')
        for row in bed:
            writer.writerow(row)

def accessSpeciesGenes(genes,SpeciesAccessions, BED):
    geneInfo ={}
    accessionToIndex={}
    indexToAccession = {}
    index = 0
    with open(genes) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            indexToAccession[index]=row[0] 
            accessionToIndex[row[0]] = index
            index+=1 
            geneInfo[row[0]] = [row[0],row[1],row[2],row[3],row[4],row[5]]
    
    for accession in SpeciesAccessions:
        current = accession[0]
        try:
            currentIndex = accessionToIndex[current]
            current = geneInfo[current]
        except KeyError:
            print("ERROR", current, "Not found in mapping check if query") 
            continue 
        
        BED.append([current[1],current[2],current[3],current[0],"100",current[4]])
        
    return BED

#create bed of common fasta

fasta = sys.argv[1]
CROVV = sys.argv[2]
NAJNA = sys.argv[3]
NOTSC = sys.argv[4]
PSETE = sys.argv[5]
HYDCUR = sys.argv[6]
BOACO = sys.argv[7]
prefix = sys.argv[8]
CrovvList = []
NajnaList = []
NotscList = []
PseteList = []
HydcurList = []
BoacoList = [] 

speciesAccession = {}

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
        if spec == "CROVV":
            CrovvList.append([accession,"",""])
        elif spec == "NAJNA":
            NajnaList.append([accession,"",""])
        elif spec == "PSETE":
            PseteList.append([accession,"",""])
        elif spec == "NOTSC":
            NotscList.append([accession,"",""])
        elif spec == "HYDCUR":
            HydcurList.append([accession,"",""])
        elif spec == "BOACO":
            BoacoList.append([accession,"",""])
        else:
            print(accession, "not in specis list")



        #print(ID,accession)


CrovvBED = []
NajnaBED = []
NotscBED = []
PseteBED = []
HydcurBED = []
BoacoBED = [] 



CrovvBED = accessSpeciesGenes(CROVV,CrovvList,CrovvBED)
print("\n\nNAJNA GENES\n\n")
NajnaBED = accessSpeciesGenes(NAJNA,NajnaList,NajnaBED)
print("\n\nNOTSC GENES\n\n")
NotscBED = accessSpeciesGenes(NOTSC,NotscList,NotscBED)
print("\n\nPSETE GENES\n\n")
PseteBED = accessSpeciesGenes(PSETE,PseteList,PseteBED)
print("\n\nHYDCUR GENES\n\n")
HydcurBED = accessSpeciesGenes(HYDCUR,HydcurList,HydcurBED)
print("\n\nBOACO GENES\n\n")
BoacoBED = accessSpeciesGenes(BOACO,BoacoList,BoacoBED)


writeBed(CrovvBED,prefix+".CROVV.bed")
writeBed(NajnaBED,prefix+".NAJNA.bed")
writeBed(NotscBED,prefix+".NOTSC.bed")
writeBed(PseteBED,prefix+".PSETE.bed")
writeBed(HydcurBED,prefix+".HYDCUR.bed")
writeBed(BoacoBED,prefix+".BOACO.bed")
