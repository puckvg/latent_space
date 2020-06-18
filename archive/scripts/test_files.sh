#!/usr/bin/env bash

# test all files terminated normally 
count=0 
for file in *.log; do 
if grep -q "Normal termination" "$file";  then
((count=count+1))
else
echo $file
echo "no normal termination"
fi
done
echo $count
