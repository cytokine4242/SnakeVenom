#!/bin/bash 


for file in *
do
    name=$(basename $file .gff)
    mkdir ${name}_Extracts
    egrep -v "^#" $file |grep -P "gene\t" | cut -f4,5,7,9 | sed -r 's/(.*)ID=([^;]*);.*/\2\t\1/g' > ${name}_Extracts/${name}.gene.txt
    egrep -v "^#" $file |grep -P "mRNA\t" | cut -f9 | egrep "Parent=" | sed -r 's/.*ID=([^;]*);.*Parent=([^;]*);.*/\1\t\2/g' |uniq > ${name}_Extracts/${name}.RNA.txt
    egrep -v "^#" $file |grep -P "CDS\t" | cut -f9 | egrep "protein_id=" | egrep "Parent=" | sed -r 's/.*Parent=([^;]*);.*product=([^;]*);.*protein_id=([^;*])/\1\t\2\t\3/g' | uniq | cut -f1 -d";"  > ${name}_Extracts/${name}.CDS.txt



done 

