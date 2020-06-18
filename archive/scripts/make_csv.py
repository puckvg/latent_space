#!/usr/bin/env python

import csv 
from glob import glob 
import gaussian
import os 

def get_molecule_name(in_file):
    name,_ = os.path.splitext(in_file)
    molecule_name = name.split("/")[-1]
    return molecule_name 

def get_properties(in_file):
    name = get_molecule_name(in_file)
    properties = gaussian.read_properties_b3lyp(in_file)
    return name, properties

if __name__=="__main__":

    directory = "../log/"
    dicts = []
    names = ['ID']

    for in_file in sorted(glob(directory+"*.log")):

        name, properties = get_properties(in_file)
        names.append(name)
        dicts.append(properties)

    with open("qm9_properties.csv", "w") as out_file:
        writer = csv.writer(out_file, delimiter="\t")
        writer.writerow(names)
        for key in dicts[0].keys(): # all keys are the same 
            writer.writerow([key] + [d[key] for d in dicts])
