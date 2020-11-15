#!/bin/bash 
#loop through all fastas to count number of non query protiens and species
ls *.fas
fastas=$(ls *.fas)
#echo $fastas
out=$1
for fasta in $fastas
do
    echo $fasta
    basename=$(basename $fasta .fas)
    #echo $basename
    python3 /mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom/UniqeCount.py \
        /mnt/e/work/hons/SnakeVenom-Feb20/Data/2020-02-25.FamilyProtiens/2020-03-05.proteinFamilyV3.fas \
        ${fasta} >  ${out}/${basename}.count.txt
done