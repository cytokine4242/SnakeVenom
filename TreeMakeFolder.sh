
#MSA 

out=$1
fasta=$(ls *.fas)
zero=0
for i in $fasta
do

    date=$(basename $i .fas)
    name=${date:11}
    clustalw2 -infile=${i} -BOOTSTRAP=1000
	

done 

