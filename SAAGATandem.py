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




def searchTandem(down,up,cords):
    tandem = False
    try:
        currGene = cords[up]
    except KeyError:
        print(up, "not in bed")
        return tandem
    #   print(currGene)
    upstream = currGene[3]
    
    geneCheck = cords[up]
    try:
        geneCheck = cords[geneCheck[-1]]
    except KeyError:
        print("first gene")
        return tandem
    NewUpstream = geneCheck[3]
    while NewUpstream == upstream:
        try:
            geneCheck = cords[geneCheck[-1]]
        except KeyError:
            print("first gene")
            return tandem
        print("upstream pos =", upstream, "downstream pos = ",NewUpstream)
        NewUpstream = geneCheck[3]

    if (geneCheck[1] == currGene[1]) and (geneCheck[0] == down):
        tandem = True
        print("2=",cords[up])
        print("1=",cords[down])
    return tandem



bed = sys.argv[1]
SAGGA = sys.argv[2]
outPref = sys.argv[3]
cords ={}
out=[]
with open(bed) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    version = .1
    prev=0
    for row in csv_reader:
        row.append(prev)
        cords[row[0]] = row
        prev = row[0]




tandemGenes = []
with open(SAGGA) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for row in csv_reader:
        tandem = searchTandem(row[0], row[1], cords)
        if tandem == True:
            tandemGenes.append([row[0],row[1]])

with open(outPref + ".tandem.pairs.txt","w") as csv_file: 
        writer = csv.writer(csv_file,delimiter='\t')
        for row in tandemGenes:
            writer.writerow(row)
       
with open(outPref + ".tandem.genes.txt", 'w') as filehandle:
    for row in tandemGenes:
        filehandle.write('%s\n' % row[0])
        filehandle.write('%s\n' % row[1])
        

#try:
#try:
         #   print(row)
        #     upstream = scaffold[row[0]+":"+str(version)][1]
      #      count = scaffold[row[0]+":"+str(version)][2]
     #       print("1.downstream =",downstream,"upstream= ", upstream )
    #        oldup = int(upstream)
   #         if int(row[1]) < int(downstream):
  #              downstream = int(row[1])
 #           if int(row[2]) > int(upstream):
#                upstream = int(row[2])
          #  print("2.downstream =",downstream,"upstream= ", upstream )
         #   print("calc", int(row[1])-int(oldup),downstream,oldup)
        #    if int(row[1])-int(oldup)  > 150000:
       #         print("increment")
      #          version += .1
     #           scaffold[row[0]+":"+str(version)] = [row[1],row[2],1]
    #            print("success")
   #         else:
  #              scaffold[row[0]+":"+str(version)] = [downstream,upstream,count+1]
 #           print("added to bed", scaffold[row[0]+":"+str(version)])
#
 #       except KeyError:
#            scaffold[row[0]+":"+str(version)] = [row[1],row[2],1]
        
