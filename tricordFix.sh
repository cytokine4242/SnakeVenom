#!/bin/bash 
file=$1
lines=$(grep -o ":[^)(]*:[^)(]*:" $file | wc -l)
number=$(grep -o ":[^)(]*:[^)(]*:" $file | grep -o ":" | wc -l)

replacements=$(($number-($lines*2)))
echo "$lines"
echo "$number"
echo "$replacements"

cp $file ${file}.backup
for i in $(seq 1 $replacements)
do 
    echo "loop"
    sed -i -E "s/([^,)(]*),([^,)(]*),/(\1,\2):0.0,/i" $file    
done