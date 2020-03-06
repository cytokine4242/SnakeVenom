#!/bin/bash
#code to compress a file for backup 
file=$1
tar -cvzf ${1}.tar.gz ${1}
