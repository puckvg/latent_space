#!/usr/bin/env python3
import os 
import pandas as pd

def parse_file(filename):
    """
    return: 
        gdb index 
        b3lyp SMILES 
    """
    with open(filename, "r") as f:
        lines = [line.rstrip() for line in f]
        # keep second last line
        smiles = lines[-2]
        smiles_gdb, smiles_b3lyp = smiles.split()
    
    filename = filename.split("/")[-1]
    index = int(filename.split(".")[0])
    return index, smiles_b3lyp

def parse_stable(stable_dir):
    llists = []
    files = sorted(os.listdir(stable_dir))
    for file in files: 
        file = stable_dir + file 
        idx, smiles = parse_file(file)
        llists.append([idx, smiles, 1])
    return llists

def parse_unstable(unstable_dir):
    llists = []
    files = sorted(os.listdir(unstable_dir))
    for file in files: 
        file = unstable_dir + file 
        idx, smiles = parse_file(file)
        llists.append([idx, smiles, 0])
    return llists

if __name__ == "__main__":
    stable_dir = "../data/stable_qm9/"
    unstable_dir = "../data/unstable_qm9/"

    llists_stable = parse_stable(stable_dir)
    llists_unstable = parse_unstable(unstable_dir)
    llists = llists_stable + llists_unstable

    df = pd.DataFrame(llists, columns=["QM9 index", "SMILES", "stable"])
    df.to_csv("../stability.csv")
