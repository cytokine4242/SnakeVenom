
fasta=$(ls *.fas)
zero=0
for i in $fasta
do
    name=$(basename $i .fas)
	egrep -A1 "CROVV|HYDCUR|NAJNA|BOACO|PSETE|NOTSC" $i > /scratch/venom/SnakeVenom-Feb20/Analysis/2020-07-01.Trees/${name}.6Snake.fas

done 

