inputDir=$1
out=$2
sortedDir=$3
genomes=$4


CROVV="CROVV"
NAJNA="NAJNA"
NOTSC="NOTSC"
PSETE="PSETE"
HYDCUR="HYDCUR"
BOACO="BOACO"
for file in ${inputDir}/*.fas 
do
prefix=$(basename $file .fas) 
python3 /mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom/fastaToBed.py \
$file \
${sortedDir}/2020-07-14.CROVV.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NAJNA.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.NOTSC.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.PSETE.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-14.HYDCUR.AccessionGene.sorted.map.csv \
${sortedDir}/2020-07-16.BOACO.AccessionGene.sorted.map.csv \
${out}/${prefix}.bed &> ${out}/${prefix}.log

done

for file in ${out}/*.bed 
do
    prefix=$(basename $file .bed) 
    sort -k1,1 -k2n,2 $file > $prefix.sorted.bed
    python3 /mnt/e/work/hons/SnakeVenom-Feb20/Progs/SnakeVenom/scaffoldCords.py ${prefix}.sorted.bed $prefix > ${prefix}.tandem.bed.log
done


for file in ${out}/*.tandemRegions.bed
do
    prefix=$(basename $file .bed)
    #echo "$file"
    #echo "$genomes"
    #echo "$prefix"
    bedtools getfasta -fi $genomes -bed $file -fo ${prefix}.fasta 2> ${prefix}.er 
    head -1 ${prefix}.fasta
done

for file in ${out}/*.er
do
    prefix=$(basename $file .er)
    cut -f2,9 -d" " $file | tr -d "(" | tr -d ")" | sed "s/:/\t/g" | sed -E "s/(\t.*)-.* /\1\t/g" > ${prefix}.er.bed  
    bedtools getfasta -fi $genomes -bed ${prefix}.er.bed  -fo ${prefix}.err.fasta  
done
for file in ${out}/*.fasta
do
    prefix=$(basename $file .tandemRegions.fasta)
    echo $file
    splitFasta.sh $file $prefix
done

runGepard.sh $out 10 $out