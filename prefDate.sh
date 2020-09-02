#!/bin/bash
#prefix files and folders with the date. 
files=$(find | cut -f2- -d'/'| tail -n+2|cat )
#echo $files
find . -printf "%d %p\n"|sort -nr | cut -f2- -d" " | cut -f2- -d'/'| head -n -1 | xargs dateLoop.sh	
#for t in "${files[@]}"
#do
#	echo $t

#done


 
