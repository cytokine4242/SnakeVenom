#!/bin/bash
prefix=$2

cat $1 | awk -v p=$prefix '{
        if (substr($0, 1, 1)==">") {filename=(substr($0,2) ".fa")}
        print $0 > pfilename
}'