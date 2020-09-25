#!/bin/bash
#generate a summary of the scaffold count for plotting in R
list=$(ls *ScaffCount.txt)
for file in $list
do
    basename=$(basename $file .txt)
    egrep "{" $file | sed "s/'[^:]*//g" | sed "s/[{}:]//g" | sed "s/$/,/g" >  ${basename}.summary.txt  
done