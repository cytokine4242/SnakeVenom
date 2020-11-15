import sys
from ete3 import Tree
import re




venom = sys.argv[1]
control = sys.argv[2]
out =sys.argv[3]
venomTree = Tree(venom,quoted_node_names = True)
controlTree = Tree(control,quoted_node_names = True)

outputTree = venomTree


venomList =[]
for node in venomTree.traverse(strategy="levelorder"):
    venomList.append(node)

controlList =[]
for node in controlTree.traverse(strategy="levelorder"):
    controlList.append(node)

outputList =[]
for node in outputTree.traverse(strategy="levelorder"):
    outputList.append(node)


print(len(venomList))
print(len(controlList))
print(len(outputList))


for i in range(len(venomList)):
    #print(venomList[i].name)
    venomSupp = float(venomList[i].support) 
    controlSupp =  float(controlList[i].support)
    diff = venomSupp - controlSupp
    outputList[i].support = diff
    #print(venomSupp, controlSupp,outputList[i].support,diff)
    outputList[i].add_features(venom=venomList[i].support, control = controlList[i])

venomList =venomTree.get_leaves()


controlList =controlTree.get_leaves()

outputList = outputTree.get_leaves()


for i in range(len(venomList)):
    venomName = str(venomList[i].name)
    #print(venomName)
    
    venomNumber = float(float(venomName.split(' ')[0].strip('%'))/100)
    #print(venomNumber)

    controlName = str(controlList[i].name)
    controlNumber = float(float(controlName.split(' ')[0].strip('%'))/100)
    
    diff = venomNumber - controlNumber
    try:    #print(venomNumber , controlNumber, diff)
        outName = str(outputList[i].name.split(" ")[2])
        print(outName)
        formatted_float = "{0:.1%}".format(diff)
        outputList[i].name = formatted_float + " | " +outName 

    except: 
        a =1
outputTree.write(outfile=out)

