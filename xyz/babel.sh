#!/usr/bin/env bash 

for file in *.xyz; do 
    filename=$(basename $file)
    filename=${filename%.*}
    outfile=$filename"_reformat.xyz"
    babel -ixyz $file -oxyz $outfile 
done
