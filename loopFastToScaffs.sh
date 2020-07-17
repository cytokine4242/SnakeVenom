#!/bin/bash

code=/mnt/e//work/hons/SnakeVenom-Feb20/Progs/SnakeVenom
gff=/mnt/e/work/hons/SnakeVenom-Feb20/Data/2020-06-17.GenomeGFF
while read file;
do 
    echo $file
    name=$(basename $file .fas)
    name=${name}ScaffCount.txt
    touch $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-01.ebs10xv2.ncbi.Gnomon.gff3 $file PSETE >> $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-22.CROVV.gff $file CROVV >> $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-18.HYDCUR.updates.final.representative.gff3 $file HYDCUR >> $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-01.ts10xv2.ncbi.Gnomon.gff3 $file NOTSC >> $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-22.NAJNA.gff $file NAJNA >> $name
    python3 ${code}/FastToScaffAll.py ${gff}/2020-06-21.BOACO.gff3 $file BOACO >> $name
done < $1