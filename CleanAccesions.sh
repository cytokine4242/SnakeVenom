#!/bin/bash 

#$1 gene list
#$2 mapping file 
#$3 postion of genes out file 

while read P
do
    egrep "${P}," $2 >> $3 
    echo $P
done < $1