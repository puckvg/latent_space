#!/usr/bin/env bash

for f in *.log; do 
    if [[ `tail -1 $f | grep -L "Normal termination"` ]]; then 
        echo $f; 
    fi; 
done > check.txt

