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
#read in bed 


bed = sys.argv[1]
outPref = sys.argv[2]
scaffold ={}
out=[]
with open(bed) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    version = .1
    for row in csv_reader:
        print(version)
        try:
            print(row)
            downstream = scaffold[row[0]+":"+str(version)][0]
            upstream = scaffold[row[0]+":"+str(version)][1]
            count = scaffold[row[0]+":"+str(version)][2]
            print("1.downstream =",downstream,"upstream= ", upstream )
            oldup = int(upstream)
            if int(row[1]) < int(downstream):
                downstream = int(row[1])
            if int(row[2]) > int(upstream):
                upstream = int(row[2])
            print("2.downstream =",downstream,"upstream= ", upstream )
            print("calc", int(row[1])-int(oldup),downstream,oldup)
            if int(row[1])-int(oldup)  > 150000:
                print("increment")
                version += .1
                scaffold[row[0]+":"+str(version)] = [row[1],row[2],1]
                print("success")
            else:
                scaffold[row[0]+":"+str(version)] = [downstream,upstream,count+1]


        except KeyError:
            scaffold[row[0]+":"+str(version)] = [row[1],row[2],1]
        

        
for key in scaffold:
    if scaffold[key][2] != 1:
        total = int(scaffold[key][1])-int(scaffold[key][0])
        print(scaffold[key])
        print(total)
        percent = total/10
        print("prelow", scaffold[key][1])
        lower = int(scaffold[key][0]) - int(percent)
        print("postLow",lower)
        if lower < 0:
            lower =0
        upper = int(scaffold[key][1]) + int(percent)
        scaff = key.split(":")    
        out.append([scaff[0],lower,upper,key,"100","+"])


writeBed(out,outPref+".tandemRegions.bed")