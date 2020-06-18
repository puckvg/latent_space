#!/usr/bin/env bash

# just keep numbers
for filename in *.xyz; do 
    number=${filename##*_}
    n_filename=$(echo $number | sed -e 's:^0*::')
    mv $filename $n_filename
done
