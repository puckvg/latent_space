#!/usr/bin/env bash 
cutoff=2.5
for file in *_rmsd.txt; do 
    rmsd=$(cat $file)
    if (( $(echo "$rmsd > $cutoff" | bc -l) )); then
        echo $rmsd
    fi
done
