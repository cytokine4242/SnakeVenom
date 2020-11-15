#!/bin/bash
#loopthrough and create GroupFiles
inputDir=$1
out=$2



CROVV="CROVV"
NAJNA="NAJNA"
NOTSC="NOTSC"
PSETE="PSETE"
HYDCUR="HYDCUR"
BOACO="BOACO"
for file in ${inputDir}/*.nwk 
do
prefix=$(basename $file .tree.nwk) 
python3 /mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom/findGroupModified.py \
$file > ${out}/${prefix}.grp

done
