import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 

#check to see if the member is already present in the fasta
def CheckDup(SpeciesAccessions,validate,valid,current):
    #print("current =",current)
    #print("validate =",validate)
    
    for check in SpeciesAccessions:
        #print("check =",check)
        if validate[0] == check[0]:
            #print("already present")
            valid = "Tandem"
    
    if current[2] == validate[2]:
        #print("same start")
        valid = False
    
    if current[3] == validate[3]:
        #print("same end")
        valid = False
    
    if int(validate[3]) > int(current[3]) and int(validate[2]) < int(current[3]): 
        print(validate[3],current[3], validate[2], current[3])
        print("overlap")
        valid=False

    
    #check gene is of good enough size
    #size = int(validate[3])-int(validate[2])
    #if size < 5000:
        #valid = False 
        #print("too short")
    
    return valid


#convert list of genes to bed
def accessSpeciesGenes(genes,SpeciesAccessions, BED):
    geneInfo ={}
    accessionToIndex={}
    indexToAccession = {}
    index = 0
    outList =[]
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
    #print()

    #find all accessions in gff
    for accession in SpeciesAccessions:
        output =[]
        current = accession[0]
        try:
            currentIndex = accessionToIndex[current]
        except KeyError:
            print("ERROR", current, "Not found in mapping check if query") 
            continue 
        preIndex = accessionToIndex[current]-1
        pre = indexToAccession[preIndex]
        pre = geneInfo[pre]


        postIndex = accessionToIndex[current]+1
        post = indexToAccession[postIndex]
        post = geneInfo[post]
        current = geneInfo[current]
        

        preValid = False
        while preValid == False:
            preValid = True
            pre = indexToAccession[preIndex]
            pre = geneInfo[pre]
            print("pre =",pre)
            preValid = CheckDup(SpeciesAccessions,pre,preValid,current)
            preIndex+=-1
            #print(preValid)
            
        #print("found valid")
        postValid = False
        while postValid == False:
            postValid = True
            post = indexToAccession[postIndex]
            post = geneInfo[post]
            postValid = CheckDup(SpeciesAccessions,post,postValid,current)
            postIndex+=1
            #print(postValid)
        
        
    
        #print(postValid)
        #print("found valid")
        #check scaffold
        print("check")
        print(pre)
        if pre[1] != current[1]:
            #pre = ["NA","NA","NA","edge of scaffold","0","NA"]
            pre = "edge"
        else:
            pre = preValid
        print(post)    
        if post[1] != current[1]:
            #post = ["NA","NA","NA","edge of scaffold","0","NA"]
            post = "edge"
        else:
            post = postValid
                
        print(current,"examine")
        if (current[4] == "-" ):
            print(post)
            print(pre)
            print("flip")
            a = pre
            pre = post
            post = a
        output.append(current[0])
        output.append(pre)
        output.append(post)
        output.append(current[4])
        outList.append(output)

    return outList

        










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
print(CrovvList)
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

print(CrovvBED)
print(NotscBED)



with open(prefix + 'Crovv.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(CrovvBED)


  
with open(prefix + 'Najna.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(NajnaBED)



with open(prefix + 'Notsc.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(NotscBED)




with open(prefix + 'Psete.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(PseteBED)



with open(prefix + 'Hydcur.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(HydcurBED)



with open(prefix + 'Boaco.tandem.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows(BoacoBED)