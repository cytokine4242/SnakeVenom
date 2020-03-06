#1/bin/bash 


specCode=$( cat /scratch/venom/SnakeVenom-Feb20/Data/2020-03-03.SpecCode/2020-03-03.SpecCodes.txt)

fasta=$(ls *.fas)
zero=0
for i in $fasta
do 
	echo "${i} species stats"
	for spec in $specCode
	do
		count=$(egrep ">" $i | egrep -c "$spec")
		if [ ${count} != $zero ] 
		then 
			echo "${i}:${spec} = $count"
		fi 


	done
done 

