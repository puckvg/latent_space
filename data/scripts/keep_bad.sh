#!/usr/bin/env bash 

bad_file=$"bad_molecules.txt"
bad_dir=$"unstable_qm9/"

cp $bad_file $bad_dir
cd $bad_dir
ls -1 | sort $bad_file $bad_file - | uniq -u | xargs rm
rm $bad_file
cd ..
