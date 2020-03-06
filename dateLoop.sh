#!/bin/bash
echo "arguments are $@"
for i in "$@"
do
	
	dateAppend=$(date +%F)
	dir=$(dirname $i)
	fil=$(basename $i)
	#echo $i
	#echo "dir is $dir"
	#echo $dateAppend
	#echo $fil
	if echo "${fil}" | egrep -v -q "^[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]\."; then		
		echo "mv $i ${dir}/${dateAppend}.${fil}"
		mv $i "${dir}/${dateAppend}.${fil}"
	fi

done

 
