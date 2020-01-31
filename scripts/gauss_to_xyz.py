#!/usr/bin/env python3 

import sys
import cclib
import numpy as np
import glob
import check_properties

NAME = {1 : 'H', 6 : 'C', 7 : 'N', 8 : 'O', 9 : 'F', 17 : 'Cl', 35 : 'Br'}

def read_file(f):
    parser = cclib.io.ccopen(f)
    data   = parser.parse()

    coords   = data.atomcoords
    print(coords)
    atomnums = data.atomnos
    numAtoms = len(atomnums)

    labels = [NAME[i] for i in atomnums]
    return numAtoms, labels, coords

def write_xyz(numAtoms, labels, coords, fout):
    print(coords)
    coords = coords[-1]
    print(coords)
    f = open(fout, 'w')
    f.write(str(numAtoms))
    f.write('\n\n')
    for i in range(len(labels)):
        string = "{}\t{}\t{}\t{}\n".format(labels[i], coords[i][0], coords[i][1], coords[i][2])
        f.write(string)

def write_xyz_all(numAtoms, labels, coords_all, fout):
    f = open(fout, 'w')

    for coords in coords_all:
        f.write(str(numAtoms))
        f.write("\n\n")
        for i in range(len(labels)):
            string = "{}\t{}\t{}\t{}\n".format(labels[i], coords[i][0], coords[i][1], coords[i][2])
            f.write(string)

        f.write("\n\n")

if __name__ == "__main__":

    filename = sys.argv[1]
    fout = filename[:-4] + ".xyz"
    numAtoms, labels, coords_all = read_file(filename)
    write_xyz(numAtoms, labels, coords_all, fout)
#     in_dir = "/home/puckvg/Work/2020-latent_space/log/"
#     out_dir = "/home/puckvg/Work/2020-latent_space/xyz/"
#     for file in sorted(glob.glob(in_dir+"*.log")):
#         name = check_properties.get_molecule_name(file)
#         out_file = out_dir+name+".xyz"
#         numAtoms, labels, coords_all = read_file(file)
#         write_xyz(numAtoms, labels, coords_all, out_file)
