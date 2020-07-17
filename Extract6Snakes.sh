out=$1
fasta=$(ls *.fas)
zero=0
for i in $fasta
do

    date=$(basename $i .fas)
    name=${date:11}
	egrep -A1 "CROVV|HYDCUR|NAJNA|BOACO|PSETE|NOTSC" $i > ${out}/${name}.6Snake.fas

done 

