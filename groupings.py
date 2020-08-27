import sys
import csv
from Bio import SeqIO
from Bio.SeqIO import FastaIO
from Bio import Phylo

def get_parent(tree, child_clade):
    node_path = tree.get_path(child_clade)
    return node_path[-2]

def all_parents(tree):
    parents = {}
    for clade in tree.find_clades(order="level"):
        for child in clade:
            parents[child] = clade
    return parents

def cladeSpecies(CheckClade):
    number =0
    species =[]
    for hit in CheckClade.get_terminals():
        spec = hit.name.split('_')[1]
        if spec not in species:
            species.append(spec)
            number +=1
    return number


def numberHuman(CheckClade):
    #print(type(CheckClade))
    #print(clade.confidence)
    #print(CheckClade.clades)
    number=0
    check = CheckClade.find_clades(terminal = True, name = '.*HUMAN.*')
    #print(check)
    #print(type(check))
    number = count_iterable(check)
    return number


def numberMouse(CheckClade):
    #print(type(CheckClade))
    #print(clade.confidence)
    #print(CheckClade.clades)
    number=0
    check = CheckClade.find_clades(terminal = True, name = '.*MOUSE.*')
    #print(check)
    #print(type(check))
    number = count_iterable(check)
    return number


def checkBootstrap(CheckClade):
    return (CheckClade.confidence)


def count_iterable(i):
    return sum(1 for e in i)

def groupFamily(parent):
    print("subfamilyCount",subfamilyCount)
    Hsize = numberHuman(parent)
    #print("Hsize =",Hsize)
    stop = False
    if(Hsize > 1):
        stop = True

    Msize = numberMouse(parent)
    print("Msize =", Msize)
    #if(Msize > 1):
    #    stop = True

    
    specNumber = cladeSpecies(parent)
    print(specNumber)
    if specNumber <3:
        stop = False
    bootstrap = checkBootstrap(parent)   
    if (bootstrap == None or bootstrap < 500):
        stop = True
    return stop




fname = sys.argv[1]
trees = Phylo.read(fname, 'newick')
parents = all_parents(trees)
#print(trees)
HUMAN = []
MOUSE = []
other = []
for clade in trees.get_terminals():
    #print(clade)
    db = clade.name.split('_')[0]
    #print(db)
    spec = clade.name.split('_')[1]
    accessionList = clade.name.split('_')
    #print(accessionList)
    size =len(accessionList)
    accession = ""
    for i in range(3,size):
        accession = accession + accessionList[i] + "_"
    accession = accession[:-1]
    if spec == "HUMAN":
        HUMAN.append(clade)
    elif spec == "MOUSE":
        MOUSE.append(clade)
    else:
        other.append(clade)

#print(HUMAN)
#print()
#print(MOUSE)
subfamilies = []
subfamilyCount = 1
insubfamily =[]

print("\n\n\n\ HUMAN \n\n\n")
for clade in HUMAN:
    stop = False
    while stop == False:
        parent = parents[clade]
        
        stop = groupFamily(parent)


        if (stop == True):
            continue
        clade = parent
    #print("\n\n new sub family", subfamilyCount," \n")
    subfamilyCount +=1
    newFamily = {}
    for found in clade.get_terminals():
        #print(found.name)
        newFamily[found.name] = True
        insubfamily.append(found.name)
    #newFamily[subfamilyCount] = subfamilyCount
    #print(newFamily.keys(),"\n")
    subfamilies.append(newFamily)
    
#print(len(insubfamily))
print("\n\n\n\ MOUSE \n\n\n")

for clade in MOUSE:
    if clade.name not in insubfamily:
        print("clade is",clade.name)  
        stop = False
        while stop == False:
            parent = parents[clade]
            
            stop = groupFamily(parent)

            if (stop == True):
                continue

            clade = parent
        #print("\n\n new sub family", subfamilyCount," \n")
        subfamilyCount +=1
        newFamily ={}
        print("reset new family")
        for found in clade.get_terminals():
            #print(found.name)
            newFamily[found.name] = True
            insubfamily.append(found.name)
        #newFamily[subfamilyCount] = subfamilyCount
        #print(newFamily.keys(),"\n")
        subfamilies.append(newFamily)
        


#print(len(insubfamily))
orphan =[]
#print(len(other))
#print(len(subfamilies))
print("\n\n\n\ OTHER \n\n\n")
for clade in other:
    if clade.name not in insubfamily:
        stop = False
        while stop == False:
            parent = parents[clade]
            stop = groupFamily(parent)

            if (stop == True):
                continue
            clade = parent
        if (len(clade.get_terminals()) > 1):
            #print("\n\n new sub family", subfamilyCount," \n")
            subfamilyCount +=1
            newFamily={}
            for found in clade.get_terminals():
                #print(found.name)
                newFamily[found.name] = True
                
                #print(len(newFamily))
                insubfamily.append(found.name)
            #newFamily[subfamilyCount] = subfamilyCount
            subfamilies.append(newFamily)
            #print(newFamily.keys(),"\n")
        else:
            orphan.append(clade.name)


#print(len(orphan))
#print("results")

#print("\n\n\n\nPRINTING AFTER\n\n")
#for family in subfamilies:
#    print(family.keys(),"\n\n")



subfamilies.sort(key=len)
#print(len(subfamilies))
uniqueFamilies = []
unique =True
i =0
for family in subfamilies:
    #print(family.keys(),"\n\n")
    unique =True
    i +=1
    j = i
    while j < len(subfamilies) and unique == True:
        for query in family.keys():
            if unique == False:
                break
            #print(query,"query from", i-1, "search from ",j)
            for search in subfamilies[j].keys():
                if query == search:
                    unique = False
                    #print("found",query, search)
                    break
        j+=1
            #print(j)
    if (unique == True):
        #print("UNQUE")
        uniqueFamilies.append(family)

print(len(uniqueFamilies))

count =0





bigUnique =[]
for family in uniqueFamilies:
    number ={}
    for prot in family.keys():
        spec = prot.split('_')[1]
        number[spec] = True
    if len(number) >=3:
        bigUnique.append(family)


for family in bigUnique:
    count+=1
    print("\n\n subfamily", count)
    for prot in family.keys():
        print(prot)
        a=1


print(len(orphan))
print(len(bigUnique))