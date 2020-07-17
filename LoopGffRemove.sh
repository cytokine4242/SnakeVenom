#!/bin/bash

folders=(2020-03-27.ebs10xv2.ncbi.Gnomon.gff3_Extracts/             2020-03-27.ts10xv2.ncbi.Gnomon.gff3_Extracts/                                 2020-03-31.GCF_001077635.1_Thamnophis_sirtalis-6.0_genomic_Extracts/
2020-03-27.GCA_000516915.1_OphHan1.0_genomic_Extracts/     2020-03-30.GCF_900067755.1_pvi1.1_genomic_Extracts/                           2020-03-31.GCF_001527695.2_P.Mucros_1.0_genomic_Extracts/
2020-03-27.GCF_009769535.1_rThaEle1.pri_genomic_Extracts/  2020-03-31.GCF_000186305.1_Python_molurus_bivittatus-5.0.2_genomic_Extracts/)
spec=( PSETE OPHHA THAEL NOTSC POVIL PYTBI THASI PROMU)
echo ${spec[0]}
i=0
input=/scratch/venom/SnakeVenom-Feb20/Data/RepltileDBFilter/ReptileGenomes.prot.fa
for fold in ${folders[@]}
do
    echo $fold 
    echo ${spec[i]}
    echo ${input}
    python ~/progs/SnakeGit/GffDuplicateSearch.py \
        ${fold}*.gene.txt  \
        ${fold}*.RNA.txt \
        ${fold}*.CDS.txt \
        ${input} \
        /scratch/venom/SnakeVenom-Feb20/Data/RepltileDBFilter/ReptileGenomes.prot.${spec[i]}.fa  > ${spec[i]}.out

    input=/scratch/venom/SnakeVenom-Feb20/Data/RepltileDBFilter/ReptileGenomes.prot.${spec[i]}.fa
    i=$((i +1 ))
done

