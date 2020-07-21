#!/bin/bash

inputDir=$1
out=$2
genomeDir=$3
sortedDir=$4


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
python3 ~/progs/SnakeGit/PrePostGene.py \
$file \
${sortedDir}/2020-07-14.CROVV.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NAJNA.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NOTSC.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.PSETE.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.HYDCUR.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-16.BOACO.AccessionGene.sorted.map.csv \
${out}/${prefix}/${prefix}.bed &> ${out}/${prefix}/${prefix}.log

    for bed in ${out}/${prefix}/*.bed 
    do
        spec=$(echo $bed | rev | cut -f2 -d'.' | rev)
        acc=$(echo $bed | rev | cut -f6- -d'.'|cut -f1 -d"/" | rev)
        echo $spec
        echo $acc
        
        if [ "$spec" = "$CROVV" ]; then
            bedtools getfasta -fi ${genomeDir}/2020-06-22.CROVV.Genome.fasta -bed $bed -s -fo ${out}/${prefix}/${acc}.CROVV.PrePost.fasta
        elif  [ "$spec" = "$NAJNA" ]; then 
            bedtools getfasta -fi ${genomeDir}/2020-06-22.NAJNA.Genome.renamed.fasta -bed $bed -s -fo ${out}/${prefix}/${acc}.NAJNA.PrePost.fasta
        elif  [ "$spec" = "$NOTSC" ]; then
            bedtools getfasta -fi ${genomeDir}/2020-06-25.ts.babs.fasta -bed $bed -s -fo ${out}/${prefix}/${acc}.NOTSC.PrePost.fasta
        elif  [ "$spec" = "$PSETE" ]; then 
            bedtools getfasta -fi ${genomeDir}/2020-06-25.ebs.babs.fasta -bed $bed -s -fo ${out}/${prefix}/${acc}.PSETE.PrePost.fasta
        elif  [ "$spec" = "$HYDCUR" ]; then 
            bedtools getfasta -fi ${genomeDir}/2020-06-18.HYDCUR.Genome.fa -bed $bed -s -fo ${out}/${prefix}/${acc}.HYDCUR.PrePost.fasta
        elif  [ "$spec" = "$BOACO" ]; then 
            bedtools getfasta -fi ${genomeDir}/2020-06-23.BOACO.snake_7C_scaffolds.fa -bed $bed -s -fo ${out}/${prefix}/${acc}.BOACO.PrePost.fasta
        else 
            echo "nothing"
        fi
    done 
done
