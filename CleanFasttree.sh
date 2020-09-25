#!!/bin/bash
boot=$1
bootnum=$2
seed=$3
seednum=$4
file=$5

fasttree -boot ${bootnum} -seed ${seednum} ${file} > ${file}.multi.nwk

python3 /home/z5162865/SnakeVenom-Feb20/Progs/SnakeVenom/removeTrichotomy.py ${file}.multi.nwk ${file}.unmulti.nwk

cat ${file}.unmulti.nwk