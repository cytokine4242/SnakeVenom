#!/bin/bash 

mapping=$(cat $1)
gff=$2

out=$3
cp $2 $3
#echo "cat out"
#cat $out
for line in $mapping
do
        #cat  $out
	#echo $line
	NCBI=$(echo $line | cut -f1 -d',')
	BABS=$(echo $line | cut -f2 -d',')
	echo "$NCBI, $BABS"
	#cat $tmp
	sed -i "s/$BABS/$NCBI/g" $out 



done 
