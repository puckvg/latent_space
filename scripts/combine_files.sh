#!/usr/bin/env bash 
dir=/home/puckvg/Work/2020-latent_space/rmsd/

for file in $dir*.txt; do 
    rmsd="`cat $file`"
    echo $rmsd
    molecule_name=$(echo $file | awk -F _ '{print $1 FS $2}')
    echo $molecule_name
done
