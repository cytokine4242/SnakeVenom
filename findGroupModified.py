import sys
from ete3 import Tree
import re

def getSpecies(name):
    ID = name.split(" ")
    db = ID[0].split('_')[0]
    spec = ID[0].split('_')[1]
    #print(spec)
    return spec



def checkDuplications(self):
    for node in self.traverse():
        #print(node)
        node.add_features(duplication=False)
        clade = []
        clade = node.get_descendants(strategy='levelorder')
        #print(clade)
        if clade == [] : continue
        left = clade[0]
        right = clade[1]
        leftSide = left.get_leaves()
        rightSide = right.get_leaves()
        #print(leftSide)
        #print(rightSide)
        cladespec = []
        for s in leftSide:
            spec = getSpecies(s.name)
            if spec not in cladespec: cladespec.append(spec)
        for s in rightSide:
            spec = getSpecies(s.name)
            if spec not in cladespec: cladespec.append(spec)
        for s in leftSide:
            if node.duplication == True: break
            
            myspec = getSpecies(s.name)
            for t in rightSide:
                tspec = getSpecies(t.name)      
                if node.duplication: break
                elif (tspec == myspec):
                    #print(s,t)
                    #print(tspec,myspec)
                    #print(node)
                    node.duplication = True
                    #print("checknode",leftSide, rightSide)



def findGroups(self):
    self.add_features(subfam = [])
    for node in self.traverse():
        if node.duplication:
            clade = node.get_descendants(strategy='levelorder')
            #print(clade)
            left = clade[0]
            right = clade[1]
            node.add_features(CladeName = str(len(node.get_leaf_names())) + " seqs " + str(node.get_leaf_names()))
            self.subfam.append(node)
        subfams = self.subfam
    i=0
    for node in subfams:
        i =i+1
        print("\nGroup "+ str(i) +":",node.CladeName)
        leafs = node.get_leaves()
        for leaf in leafs:
            print(str(leaf)[3:])




nwktree = sys.argv[1]
#out= sys.argv[2]
t = Tree(nwktree,quoted_node_names = True)

checkDuplications(t)
findGroups(t)

# ```

# for node in _tree.node[:-1]:
#             #print node.info['Name']
#             if node.ancNode().opt['Duplication'] 
#                 clades = _tree._descClades(node)
#                 clades = clades[0] + clades[1]
#                 if len(clades) < _tree.stat['MinFamSize']: continue
#                 node.opt['Compress'] = True
#                 _tree.subfam.append(node)
#                 if node.info['CladeName'] == 'None':
#                     node.info['CladeName'] = '%d Seqs %s' % (len(clades),_tree.nodeList(clades))

#         ## <ii> ## Check no descendant nodes are duplications
#         fams = _tree.subfam[0:]
#         for node in fams:
#             for othernode in fams:
#                 if node in _tree.subfam and _tree._isAnc(node,othernode):
#                     node.opt['Compress'] = False
#                     _tree.subfam.remove(node)
#                     #break
#         ## <iib> ## Lineage-specific duplications ##
#         fams = _tree.subfam[0:]
#         for node in _tree.node:
#             if node in fams: continue
#             elif node.opt['SpecDup']:
#                 clades = _tree._descClades(node)
#                 clades = clades[0] + clades[1]
#                 node.opt['Compress'] = True
#                 _tree.subfam.append(node)
#                 if node.info['CladeName'] == 'None': node.info['CladeName'] = '%d Seqs %s' % (len(clades),_tree.nodeList(clades))
#                 for othernode in _tree.subfam:
#                     if node in _tree.subfam and _tree._isAnc(othernode,node):
#                         node.opt['Compress'] = False
#                         _tree.subfam.remove(node)
#                         break
#                 for othernode in _tree.subfam[0:]:
#                     if node.opt['Compress'] and _tree._isAnc(node,othernode):
#                         othernode.opt['Compress'] = False
#                         _tree.subfam.remove(othernode)
                        
#         _tree.textTree()
#         _tree.info['Grouping'] = 'dup'
                        




# for node in self.node:
#                 node.opt['Duplication'] = False
#                 if len(node.branch) > 1:    # Internal
#                     clade = self._descClades(node)
#                     cladespec = []
#                     for s in clade[0] + clade[1]:
#                         spcode = s.obj['Sequence'].info['SpecCode']
#                         if spcode not in cladespec: cladespec.append(spcode)
#                     for s in clade[0]:
#                         if node.opt['Duplication']: break
#                         elif (species == None) or (species == s.obj['Sequence'].info['Species']) or (species == s.obj['Sequence'].info['SpecCode']):
#                             myspec = s.obj['Sequence'].info['SpecCode']
#                             for t in clade[1]:
#                                 tspec = t.obj['Sequence'].info['SpecCode']
#                                 if node.opt['Duplication']: break
#                                 elif (tspec == myspec): 
#                                     node.opt['Duplication'] = True
#                 if node.opt['Duplication'] and len(cladespec) < self.stat['SpecDup'] and 'UNK' not in cladespec:
#                     node.opt['SpecDup'] = True; node.opt['Duplication'] = False

