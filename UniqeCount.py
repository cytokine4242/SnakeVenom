import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#/mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom
#count the number for each sub group of species for plotting in R
queryFile=sys.argv[1]

fasta=sys.argv[2]
m = re.search('2020-11-07.(.*).fas', fasta)
if m:
    family = m.group(1)
print(family)
queries = {}
#read in file
with open(queryFile, "r") as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        queries[record.name] = True
Vsnakes = {}
NVsnakes ={}
lizards ={}
#define familes
lizards["ANOCA"]=0
NVsnakes["BOACO"]=0
Vsnakes["CROVV"]=0
Vsnakes["DEIAC"]=0
lizards["DOPGR"]=0
Vsnakes["HYDCUR"]=0
Vsnakes["NAJNA"]=0
Vsnakes["NOTSC"]=0
Vsnakes["OPHHA"]=0
Vsnakes["PANGU"]=0
lizards["POGVI"]=0
Vsnakes["PROFL"]=0
Vsnakes["PROMU"]=0
Vsnakes["PSETE"]=0
NVsnakes["PYTBI"]=0
Vsnakes["THAEL"]=0
Vsnakes["THASI"]=0
lizards["VARKO"]=0
speciesCount={}
speciesCount["BOVIN"]=0
speciesCount["CANLF"]=0
speciesCount["CHICK"]=0
speciesCount["DANRE"]=0
speciesCount["GORGO"]=0
speciesCount["HUMAN"]=0
speciesCount["LEPOC"]=0
speciesCount["MONDO"]=0
speciesCount["MOUSE"]=0
speciesCount["ORYLA"]=0
speciesCount["PANTR"]=0
speciesCount["RAT"]=0
speciesCount["XENTR"]=0
        

numbers=[Vsnakes,NVsnakes,lizards,speciesCount]

count = 0
VsnakesCount =0
NVsnakesCount=0
lizardsCount=0
qfoCount=0
#perform the counts and appending 
with open(fasta, "r") as handle: 
    for record in SeqIO.parse(handle, "fasta"):
        
        try:
            a = queries[record.name]
            print(record.name)
            #print((record))
            ID = record.name.split(" ")
            accessionList = ID[0].split('_')[3:]
            accession="_".join(accessionList)
            #print(accession)
            if family == accession:
                familyName=record.description.split("|")[1]
            
        except KeyError:
            count+=1
            ID = record.name.split(" ")
            db = ID[0].split('_')[0]
            spec = ID[0].split('_')[1]
            try:
                Vsnakes[spec] +=1
                VsnakesCount+=1
            except KeyError:
                fail = True
            try:
                NVsnakes[spec]+=1 
                NVsnakesCount+=1
            except KeyError:
                fail = True
            try:
                lizards[spec]+=1
                lizardsCount+=1
            except KeyError:
                fail = True
            try:
                speciesCount[spec]+=1
                qfoCount+=1
            except KeyError:
                fail = True
                
            #speciesCount[spec]+=1

print(numbers)
print(familyName,"\t",count,"\t",VsnakesCount,"\t",NVsnakesCount,"\t",lizardsCount,"\t",qfoCount,)
 

#Reptiles = {}
#Reptiles["ANOCA"]=0
#Reptiles["BOACO"]=0
#Reptiles["CROVV"]=0
#Reptiles["DEIAC"]=0
#Reptiles["DOPGR"]=0
#Reptiles["HYDCUR"]=0
#Reptiles["NAJNA"]=0
#Reptiles["NOTSC"]=0
#Reptiles["OPHHA"]=0
#Reptiles["PANGU"]=0
#Reptiles["POGVI"]=0
#Reptiles["PROFL"]=0
#Reptiles["PROMU"]=0
#Reptiles["PSETE"]=0
#Reptiles["PYTBI"]=0
#Reptiles["THAEL"]=0
#Reptiles["THASI"]=0
#Reptiles["VARKO"]=0
#speciesCount={}
#speciesCount["ANOCA"]=0
#speciesCount["BOACO"]=0
#speciesCount["CROVV"]=0
#speciesCount["DEIAC"]=0
#speciesCount["DOPGR"]=0
#speciesCount["HYDCUR"]=0
#speciesCount["NAJNA"]=0
#speciesCount["NOTSC"]=0
#speciesCount["OPHHA"]=0
#speciesCount["PANGU"]=0
#speciesCount["POGVI"]=0
#speciesCount["PROFL"]=0
#speciesCount["PROMU"]=0
#speciesCount["PSETE"]=0
#speciesCount["PYTBI"]=0
#speciesCount["THAEL"]=0
#speciesCount["THASI"]=0
#speciesCount["VARKO"]=0
#speciesCount["BOVIN"]=0
#speciesCount["CANLF"]=0
#speciesCount["CHICK"]=0
#speciesCount["DANRE"]=0
#speciesCount["GORGO"]=0
#speciesCount["HUMAN"]=0
#speciesCount["LEPOC"]=0
#speciesCount["MONDO"]=0
#speciesCount["MOUSE"]=0
#speciesCount["ORYLA"]=0
#speciesCount["PANTR"]=0
#speciesCount["RAT"]=0
#speciesCount["XENTR"]=0
