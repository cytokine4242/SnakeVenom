#!/bin/bash
#summarise scaffold count into single file for R scripts

for output in *.txt
do
    base=$(basename $output .txt)
    egrep "{" $output > ${base}.analysis.txt
done