#!/bin/bash
#loopthrough and create propost
inputDir=$1
out=$2
sortedDir=$3



CROVV="CROVV"
NAJNA="NAJNA"
NOTSC="NOTSC"
PSETE="PSETE"
HYDCUR="HYDCUR"
BOACO="BOACO"
for file in ${inputDir}/*.fas 
do
prefix=$(basename $file .fas) 
mkdir ${out}/${prefix}
python3 /mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom/TandemCheck.py \
$file \
${sortedDir}/2020-07-14.CROVV.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NAJNA.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NOTSC.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.PSETE.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.HYDCUR.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-16.BOACO.AccessionGene.sorted.map.csv \
${out}/${prefix}/${prefix}.bed &> ${out}/${prefix}/${prefix}.log

done
