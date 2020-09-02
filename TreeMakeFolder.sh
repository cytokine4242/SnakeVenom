
#!/bin/bash 
#make a indiviudal clustal tree for eah file in a folder
out=$1
fasta=$(ls *.fas)
zero=0
for i in $fasta
do

    date=$(basename $i .fas)
    name=${date:11}
    clustalw2 -infile=${i} -BOOTSTRAP=1000
	

done 

