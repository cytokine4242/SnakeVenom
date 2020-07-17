import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 



def writeBed(bed,name):
    with open(name, 'w') as csv_file:  
        writer = csv.writer(csv_file,delimiter='\t')
        for row in bed:
            writer.writerow(row)

def CheckDup(SpeciesAccessions,validate,valid,current):
    print("current =",current)
    print("validate =",validate)
    
    for check in SpeciesAccessions:
        #print("check =",check)
        if validate[0] == check[0]:
            print("already present")
            valid = False
    
    if current[2] == validate[2]:
        print("same start")
        valid = False
    
    if current[3] == validate[3]:
        print("same end")
        valid = False
    
    if validate[3] > current[3] and validate[2] < current[3]: 
        print("overlap")
        valid=False

    
    
    size = int(validate[3])-int(validate[2])
    if size < 5000:
        valid = False 
        print("too short")
    
    return valid



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
    
    
    current = ""
    pre = ""
    post = ""
    print()
    for accession in SpeciesAccessions:
        current = accession[0]
        currentIndex = accessionToIndex[current]
        preIndex = accessionToIndex[current]-1
        pre = indexToAccession[preIndex]
        pre = geneInfo[pre]


        postIndex = accessionToIndex[current]+1
        post = indexToAccession[postIndex]
        post = geneInfo[post]
        current = geneInfo[current]
        
        valid = False
        
        while valid == False:
            valid = True
            pre = indexToAccession[preIndex]
            pre = geneInfo[pre]
            valid = CheckDup(SpeciesAccessions,pre,valid,current)
            preIndex+=-1
            print(valid)
            
        print("found valid")
        valid = False
        while valid == False:
            valid = True
            post = indexToAccession[postIndex]
            post = geneInfo[post]
            valid = CheckDup(SpeciesAccessions,post,valid,current)
            postIndex+=1
            print(valid)
        print("found valid")
        print(pre[1])
        print(current[1])
        if pre[1] != current[1]:
            #pre = ["NA","NA","NA","edge of scaffold","0","NA"]
            pre = False
        if post[1] != current[1]:
            #post = ["NA","NA","NA","edge of scaffold","0","NA"]
            post = False
                
        
        accession[1] = pre
        accession[2] = post
        
    for accession in SpeciesAccessions:
        #print(accession)
        print(accession[0])
        print("going into if")
        print("1",accession[1])
        print("2",accession[2])
        #BED.append([accession[0][1],accession[0][2],accession[0][3],accession[0][0]])
        if accession[1] != False:
            print("inside 1",accession[1])
            BED.append([accession[1][1],accession[1][2],accession[1][3],"pre-"+accession[0]+";"+accession[1][0],"100",accession[1][4]])
        if accession[2] != False:
            print("inside 2", accession[2])
            BED.append([accession[2][1],accession[2][2],accession[2][3],"post-"+accession[0]+";"+accession[2][0],"100",accession[2][4]])

    return BED

        










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
print("\n\nCROVV GENES\n\n")
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
