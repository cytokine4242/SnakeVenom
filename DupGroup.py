import sys
import csv
from Bio import SeqIO
from Bio.SeqIO import FastaIO
from Bio import Phylo
import re
import pylab



def findLineage(speciesList):

    Vsnakes = {}
    NVsnakes ={}
    lizards ={}
    #define familes
    lizards["ANOCA"]= False
    NVsnakes["BOACO"]= False
    Vsnakes["CROVV"]= False
    Vsnakes["DEIAC"]= False
    lizards["DOPGR"]= False
    Vsnakes["HYDCUR"]= False
    Vsnakes["NAJNA"]= False
    Vsnakes["NOTSC"]= False
    Vsnakes["OPHHA"]= False
    Vsnakes["PANGU"]= False
    lizards["POGVI"]= False
    Vsnakes["PROFL"]= False
    Vsnakes["PROMU"]= False
    Vsnakes["PSETE"]= False
    NVsnakes["PYTBI"]= False
    Vsnakes["THAEL"]= False
    Vsnakes["THASI"]= False
    lizards["VARKO"]= False
    speciesCount={}
    speciesCount["BOVIN"]= False
    speciesCount["CANLF"]= False
    speciesCount["CHICK"]= False
    speciesCount["DANRE"]= False
    speciesCount["GORGO"]= False
    speciesCount["HUMAN"]= False
    speciesCount["LEPOC"]= False
    speciesCount["MONDO"]= False
    speciesCount["MOUSE"]= False
    speciesCount["ORYLA"]= False
    speciesCount["PANTR"]= False
    speciesCount["RAT"]= False
    speciesCount["XENTR"]= False
        
    for species in speciesList:
        qfoBol = False
        try: 
            speciesCount[species] = True
            qfo = True
        except Exception:
            pass 
        VsnkaesBol = False
        try: 
            Vsnakes[species] = True
            qfo = True
        except Exception:
            pass 
        lizardBol = False
        try: 
            lizards[species] = True
            qfo = True
        except Exception:
            pass
        NVsnkaesBol = False
        try: 
            NVsnakes[species] = True
            qfo = True
        except Exception:
            pass


speciesMap ={
"ANOCA":"Anolis_carolinensis",
"CROVV":"Crotalus_viridis",
"DEIAC":"Deinagkistrodon_acutus",
"DOPGR":"Dopasia_gracilis",
"NOTSC":"Notechis_scutatus",
"OPHHA":"Ophiophagus_hannah",
"POGVI":"Pogona_vitticeps",
"PROMU":"Protobothrops_mucrosquamatus",
"PSETE":"Pseudonaja_textilis",
"PYTBI":"Python_bivittatus",
"THASI":"Thamnophis_sirtalis",
"HYDCUR":"Hydrophis_curtus",
"VARKO":"Varanus_komodoensis",
"NAJNA":"Naja_naja",
"PANGU":"Pantherophis_guttatus",
"THAEL":"Thamnophis_elegans",
"BOACO":"Boa_constrictor",
"PROFL":"Protobothrops_flavoviridis",
"BOVIN":"Bos_taurus",
"CANLF":"Canis_lupus",
"CHICK":"Gallus_gallus",
"DANRE":"Danio_rerio",
"GORGO":"Gorilla_gorilla",
"HUMAN":"Homo_sapiens",
"LEPOC":"Lepisosteus_oculatus",
"MONDO":"Monodelphis_domestica",
"MOUSE":"Mus_musculus",
"ORYLA":"Oryzias_latipes",
"PANTR":"Pan_troglodytes",
"RAT":"Rattus_norvegicus",
"XENTR":"Xenopus_tropicalis"
}


fname = sys.argv[1]
tree = Phylo.read(fname, 'newick')
group = sys.argv[2]
out= sys.argv[3]



groups=[]
newGroup ={}
with open(group) as file_in:
    for line in file_in:
        #print(line)
        if (line != "\n"):
            #print(line)
            m = re.search('Group', line)
            if m:
                groups.append(newGroup)
                newGroup ={}
            else:
                #print(line)
                spec = line.split('_')[1]
                try:
                    a =speciesMap[spec]
                    newGroup[spec] = True
                except KeyError:
                    print(line, " is query")
groups.append(newGroup)
groups.pop(0)
#print(groups)


#print(type(tree))
#print(type(tree.clade))
root = tree.clade

Phylo.write(tree,out+"original.nwk", "newick")
for node in root.get_nonterminals():
    #print(node.confidence)
    node.confidence = 0

for node in root.get_terminals():
    node.confidence = 0



leafs = {}
leafDup ={}
for leaf in root.get_terminals():
    leafs[leaf] = False
    leafDup[leaf.name] =0

i =0
for group in groups:
    i +=1
    #print("Group ", i)
    speciesList =list(group.keys())
    #print(speciesList)
    latin=[]
    leafs = dict.fromkeys(leafs, False)
    #print("lentght is",len(speciesList),speciesList)
    if len(speciesList) == 1:
        #print("inside")
        species = speciesList[0]
        latinName =speciesMap[species]
        #print(latinName)
        leafDup[latinName]+=1
        print("Group ",i,"\t",1,"\t", 1,"\t",0,"\t",1)
    else:  
        for species in speciesList:
            latin.append(speciesMap[species])
            node = speciesMap[species]
            #print(node) 
            leafs[node] = True
        
        search = [keys for keys,v in leafs.items() if v == True]
        #print(search)
        number =root.common_ancestor(search).confidence
        #print(number)
        root.common_ancestor(search).confidence = number +1

        common = root.common_ancestor(search)
        
        lineage = findLineage(speciesList)
        
        
        
        nLeafs =0 
        for terminal in common.get_terminals():
            nLeafs +=1
        diff = nLeafs - len(search)
        percent = len(search)/nLeafs
        print("Group ",i,"\t",nLeafs,"\t", len(search),"\t",diff,"\t",percent)

        

for leaf in root.get_terminals():
    name = leaf.name
    #print(name) 
    name = name+" ("+str(leafDup[leaf.name])+")"
    #print(name)
    leaf.name = name
Phylo.write(tree,out, "newick")
