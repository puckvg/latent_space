#!/usr/bin/env bash

qm9_dir=/home/puckvg/Data/C7H10O2_xyz/
b3lyp_dir=/home/puckvg/Work/2020-latent_space/xyz/
out_dir=/home/puckvg/Work/2020-latent_space/rmsd/

for qm9_file in $qm9_dir*.xyz; do
    name=$(basename $qm9_file)
    molecule=$(echo $name | cut -f 1 -d '.')
    echo $molecule

    b3lyp_file=$b3lyp_dir$molecule".xyz"
    out=$out_dir$molecule"_rmsd.txt"
    ./calculate_rmsd.py $qm9_file $b3lyp_file > $out 
done
