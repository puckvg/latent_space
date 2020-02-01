#!/usr/bin/env python3 
"""
Asserting the following properties are unchanged...
"A"
"B"
"C"
"mu"
"alpha"
"homo"
"lumo"
"gap"
"r2"
"zpve"
"u0"
"u"
"h"
"g"
"cv"
"SMILES"
"""

property_indices = {0:"A", 1:"B", 2:"C", 3:"mu", 4:"alpha", \
                    5:"homo", 6:"lumo", 7:"gap", 8:"r2", \
                    9:"zpve", 10:"u0", 11:"u", 12:"h", \
                    13:"g", 14:"cv", 15:"SMILES"}

import parse_QM9
import gaussian 
from glob import glob 
import os 
import gauss_to_xyz
import pybel
import rdkit 
from rdkit import Chem 

def percent_diff(i,j):
    if (i+j)!=0:
        x = abs(i-j)/(0.5*(i+j))
        x = x*100
    else:
        if i==j:
            x= 0
    return x

def xyz2smiles(xyz_file):
    for mol in pybel.readfile("xyz",xyz_file):
       mol = str(mol)
       smiles, file = mol.split()
    return smiles

def get_original_properties(qm9_file):
    mol = parse_QM9.Molecule(qm9_file)
    mol.parse_file()
    smiles = mol.properties["SMILES"]
    return mol.properties

def get_molecule_name(file):
    name,_ = os.path.splitext(file)
    molecule_name = name.split("/")[-1]
    return molecule_name

def get_b3lyp_properties(gauss_file,xyz_file):
    properties = gaussian.read_properties_b3lyp(gauss_file)
   # print("read properties ok")
    del properties["imaginary_frequency_count"]

    smiles = xyz2smiles(xyz_file)
    #print("convert xyz 2 smiles")
    properties["SMILES"]=smiles
    return properties

def read_rmsd(file):
    with open(file, "r") as f:
        lines = f.readlines()
    try:
        rmsd = float(lines[0])
    except:
        print(file)
        print(lines)
        return None
    return rmsd 

def check_rmsd(rmsd, threshold=0.25):
    if rmsd > threshold:
        return False
    else:
        return True 

def compare_dictionaries(dict1, dict2, key, threshold=1):
    pairs = zip(dict1[key], dict2[key])

    for idx, (i,j) in enumerate(pairs):
        if type(i)==float and type(j)==float:
                if percent_diff(i,j)<=threshold:
                    pass
                else:
                    pass
                  #  print("property ",property_indices[idx], \
                   #     "doesn't match with values,",i," and",j)
#                    with open("failed_b3lyp_properties.txt","a") as f:
#                        f.write(key)
#                        f.write("   ")
#                        f.write(property_indices[idx])
#                        f.write("   ")
#                        f.write("\n")
        elif type(i)==str and type(j)==str:
            if i==j:
                return True
            else:
                print(i)
                print(j)
                return False


if __name__=="__main__":
    QM9_dir = "/home/puckvg/Data/C7H10O2/"
    B3LYP_dir = "/home/puckvg/Work/2020-latent_space/log/"
    B3LYP_xyz_dir = "/home/puckvg/Work/2020-latent_space/xyz/"
    rmsd_dir = "/home/puckvg/Work/2020-latent_space/rmsd/"

    properties_qm9 = {}
    properties_b3lyp = {}
    rmsd_dict = {}

    for file_qm9 in sorted(glob(QM9_dir+"*.xyz")):
        #print("qm9 file, ", file_qm9)
        qm9_name = get_molecule_name(file_qm9)

        original_properties = get_original_properties(file_qm9) 
        properties_qm9[qm9_name] = list(original_properties.values())

        # read RMSD
        rmsd_file = rmsd_dir+qm9_name+"_rmsd.txt"
        rmsd = read_rmsd(rmsd_file)
        rmsd_dict[qm9_name]=rmsd

    for file in glob(B3LYP_dir+"*.log"):

        name = get_molecule_name(file)
        xyz_file = B3LYP_xyz_dir+name+".xyz"
        # want xyz file for smiles matching (which doesn't work right now anyway)
        b3lyp_properties = get_b3lyp_properties(file,xyz_file) 
        properties_b3lyp[name] = list(b3lyp_properties.values())

    # compare dictionaries 
    for molecule in properties_b3lyp.keys():
        #print(molecule)
        boolean=compare_dictionaries(properties_b3lyp, properties_qm9, molecule) 
        if boolean==False:
            print(molecule)

