#!/usr/bin/env bash 

bad_file=$"bad_molecules.txt"
good_dir=$"stable_qm9/"

for fname in $(cat $bad_file); do 
    rm $good_dir$fname".xyz"
done
