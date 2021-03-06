import sys
import csv
from Bio import SeqIO
from Bio.SeqIO import FastaIO
from Bio import Phylo
# get the parent node of a node
def get_parent(tree, child_clade):
    node_path = tree.get_path(child_clade)
    return node_path[-2]
#create a dictionary of all parent nodes and childs
def all_parents(tree):
    parents = {}
    for clade in tree.find_clades(order="level"):
        for child in clade:
            parents[child] = clade
    return parents
#count the number of species in a sub tree
def cladeSpecies(CheckClade):
    number =0
    species =[]
    for hit in CheckClade.get_terminals():
        spec = hit.name.split('_')[1]
        if spec not in species:
            species.append(spec)
            number +=1
    return number

#count the number of human protiens in a sub tree
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

#count the number of mouse protiens in a sub tree
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

#access the bootstrap number
def checkBootstrap(CheckClade):
    return (CheckClade.confidence)

#count the size
def count_iterable(i):
    return sum(1 for e in i)

#look up if a subtree is max size for a group
def groupFamily(parent):
    print("subfamilyCount",subfamilyCount)
    Hsize = numberHuman(parent)
    #print("Hsize =",Hsize)
    stop = False
    #if(Hsize > 1):
    #stop = True

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


#read in

fname = sys.argv[1]
trees = Phylo.read(fname, 'newick')
parents = all_parents(trees)
#print(trees)

leaves = []
#iterate through leaves to get protiens
for clade in trees.get_terminals():
 
    leaves.append(clade)
subfamilies = []
subfamilyCount = 1
insubfamily =[]
orphan =[]
#iterate through entire tree looking for families
for clade in leaves:
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


subfamilies.sort(key=len)
#print(len(subfamilies))
uniqueFamilies = []
unique =True
i =0

#double check for duplicate families 
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




#get biggest familes 
bigUnique =[]
for family in uniqueFamilies:
    number ={}
    for prot in family.keys():
        spec = prot.split('_')[1]
        number[spec] = True
    if len(number) >=3:
        bigUnique.append(family)
    else:
        for prot in family.keys():
            orphan.append(prot)

#print families 
for family in bigUnique:
    count+=1
    print("\n\n subfamily", count)
    for prot in family.keys():
        print(prot)
        a=1


print(len(orphan))
print(len(bigUnique))