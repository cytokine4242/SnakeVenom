#!/bin/bash

date=$(date +%F)
dir=~/Backup/${date}.Backup
mkdir $dir 
for i in $@
do
	cp $i ${dir}/
	echo "cp $i $dir/"


done






