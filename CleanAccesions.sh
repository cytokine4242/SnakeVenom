#!/bin/bash 


while read P
do
    egrep "${P}," $2 >> $3 
    echo $P
done < $1