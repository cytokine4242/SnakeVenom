import sys
import csv
import re
from Bio import SeqIO
from Bio.SeqIO import FastaIO 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#count the number of scaffolds for each of the 6 snake species 
counts=sys.argv[1:]
print(counts)
CrovvCount = []
NajnaCount = []
NotscCount = []
PseteCount = []
HydcurCount = []
BoacoCount = [] 
#run through and count so can by used in R somehomw
for analysis in counts:
    print(analysis)
    with open(analysis) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            #print(csv_reader)
            line =0
            for row in csv_reader:

                line +=1
                for col in row:
                    info=col.split(':')
                    #print(info)
                    try:
                        info=info[1]
                    except:
                        continue
                    info = re.sub("\D", "", info)
                    info = re.sub("}", "", info)
                    #print(info)
                    if line ==1:
                        PseteCount.append(int(info))
                        
                    elif line ==2:
                        CrovvCount.append(int(info))
                    elif line ==3:
                        HydcurCount.append(int(info))
                    elif line ==4:
                        NotscCount.append(int(info))
                    elif line ==5:
                        NajnaCount.append(int(info))
                    elif line ==6:
                        BoacoCount.append(int(info))
                    else:
                        print("broke")

print(CrovvCount) 
print(NajnaCount) 
print(NotscCount) 
print(PseteCount) 
print(HydcurCount)
print(BoacoCount) 


print(range(max(CrovvCount)))
plt.hist(CrovvCount, align='left',bins=(max(CrovvCount)))
plt.ylabel('No of times')
plt.savefig('foo.png')