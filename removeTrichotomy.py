import sys
from ete3 import Tree



nwktree = sys.argv[1]
out= sys.argv[2]
t = Tree(nwktree)
t.resolve_polytomy()
t.write(format=1, outfile=out)

