#!/usr/bin/env python3
import glob

class Molecule:

    def __init__(self, file):
        self.file = file

    def parse_file(self):
        with open(self.file) as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]

        self.nAtoms = int(lines[0])

        # see https://www.nature.com/articles/sdata201422/tables/4 for properties
        tag,i,self.A,self.B,self.C,self.mu, \
        self.alpha,self.homo,self.lumo,self.gap, \
        self.r2,self.zpve,self.u0, \
        self.u,self.h,self.g,\
        self.cv=lines[1].split()

        self.InChI_Corina, self.InChI_B3LYP = lines[-1].split()
        self.SMILES_GDB, self.SMILES_B3LYP = lines[-2].split()
        self.harmonic_vib_frequencies = lines[-3].split()

        self.coordinates=[]
        self.elements=[]
        l = len(lines)
        for idx,line_number in enumerate(range(2, l-3)):
            element_type, x, y, z, mulliken_partial_charge = lines[line_number].split()
            self.elements.append(element_type)
            self.coordinates.append((x,y,z))


        self.properties={}
        self.properties["A"]=float(self.A)
        self.properties["B"]=float(self.B)
        self.properties["C"]=float(self.C)
        self.properties["mu"]=float(self.mu)
        self.properties["alpha"]=float(self.alpha)
        self.properties["homo"]=float(self.homo)
        self.properties["lumo"]=float(self.lumo)
        self.properties["gap"]=float(self.gap)
        self.properties["r2"]=float(self.r2)
        self.properties["zpve"]=float(self.zpve)
        self.properties["u0"]=float(self.u0)
        self.properties["u"]=float(self.u)
        self.properties["h"]=float(self.h)
        self.properties["g"]=float(self.g)
        self.properties["cv"]=float(self.cv)
        self.properties["SMILES"]=self.SMILES_B3LYP

    def write_xyz(self,out_file):
        with open(out_file, "w") as f:
            f.write(str(self.nAtoms))
            f.write("\n\n")
            for element, (x,y,z) in zip(self.elements, self.coordinates):
                f.write(element)
                f.write("   ")
                f.write(str(x))
                f.write("   ")
                f.write(str(y))
                f.write("   ")
                f.write(str(z))
                f.write("\n")

if __name__=="__main__":
    for file in glob.glob("/home/puckvg/Data/C7H10O2/*.xyz"):
        print(file)
        name = file.split("/")[-1]
        out_dir = "/home/puckvg/Data/C7H10O2_xyz/"
        out_file = out_dir+name
        mol = Molecule(file)
        mol.parse_file()
        mol.write_xyz(out_file)

