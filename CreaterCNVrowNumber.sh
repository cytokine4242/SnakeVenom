#!/bin/bash
AccessionList=$1
mapping=$2
cnvTable=$3
out=$4

declare -A my_array
while read Accession; do
    name=$(echo "$Accession" | cut -f4- -d_ | cut -f1 -d" ")
    echo "name $name"
    searchAtrribute=$(egrep "$name" $mapping | cut -f6 -d, |cut -f2 -d'"' | cut -f1 -d";")
    echo "search $searchAtrribute"
    if [ -z "$searchAtrribute" ]
    then
        echo "$searchAtrribute is NOT found"
    else
        linenumber=$(egrep -n "${searchAtrribute};" $cnvTable | cut -f1 -d":")
        echo "line $linenumber"
        echo "$linenumber,$searchAtrribute">> ${out}.tmp
    fi
    
done <${AccessionList}


sort ${out}.tmp | uniq > $out

rm ${out}.tmp


