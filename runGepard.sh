#!/bin/bash 
inputDir=$1
light=$2
out=$3


for file in ${inputDir}/*.fa
do
prefix=$(basename $file .fa) 
echo "gepard ${file}"
java -Xmx12g -cp /mnt/e/work/hons/SnakeVenom-Feb20/Progs/Gepard-1.40.jar org.gepard.client.cmdline.CommandLine  -seq1 $file -seq2 $file -lower $light -matrix /mnt/e/work/hons/SnakeVenom-Feb20/Progs/matrix -outfile ${out}.${prefix}.png

done