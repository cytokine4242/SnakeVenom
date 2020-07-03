

#MSA 

out=$1
fasta=$(ls *.fas)
zero=0
for i in $fasta
do

    date=$(basename $i .fas)
    name=${date:11}
	python /share/apps/slimsuite/tools/seqsuite.py seq -seqin $i -align -alnprog clustalo -seqout ${1}/${name}.fas

done 

