#!/bin/bash
#egrep ">" * | cut -f2- -d":"  | cut -f1 -d" " | cut -f4- -d"_" > ../2020-10-29.MMseq/results/venom.genes.txt#
snake=BOACO
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt

snake=CROVV
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt

snake=HYDCUR
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt

snake=PSETE
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt

snake=NOTSC
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt

snake=NAJNA
python3 ../../../Progs/SnakeVenom/SAAGATandem.py ${snake}.genes.position.sorted.csv ${snake}.tbl ${snake} > ${snake}.log
sort ${snake}.tandem.genes.txt | uniq > ${snake}.tandem.uniq.txt
cat ${snake}.tandem.uniq.txt venom.genes.txt | sort | uniq -c | egrep -v "^[ ]*1" > ${snake}.tandemVenom.txt