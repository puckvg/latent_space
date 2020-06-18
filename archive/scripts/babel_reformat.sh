#!/usr/bin/env bash 

in_dir=../xyz/
out_dir=../xyz_reformat/

for file in ../xyz/*.xyz; do 
    name=$(basename "$file")
    molecule_name="${name%.*}"
    babel -ixyz $file -oxyz $out_dir$name
done
