#!/usr/bin/env python3

import gaussian
from glob import glob
import os

def get_im_freq(file):
    properties = gaussian.read_properties_b3lyp(file)
    n = properties["imaginary_frequency_count"]
    return n 

def get_molecule_name(in_file):
    name,_ = os.path.splitext(in_file)
    molecule_name = name.split("/")[-1]
    return molecule_name

def write_to_file(tuple_list):
    with open("imaginary_frequencies.txt", "w") as f:
        f.write('\n'.join('%s %s' % x for x in tuple_list))

if __name__=="__main__":

    directory = "/home/puckvg/Work/2020-latent_space/log/"
    tuple_list = []

    for file in glob(directory+"*.log"):
        name = get_molecule_name(file)
        n = get_im_freq(file)
        tuple_list.append((name, n))


    write_to_file(tuple_list) 

