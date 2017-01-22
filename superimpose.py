import Bio
from Bio import PDB
from Bio.PDB import *
a=[]
b=[]
c=[]
parser=PDB.PDBParser(PERMISSIVE=1)
s=parser.get_structure("4w52","4w52.pdb")
for model in s:
    for chain in model:
        for residue in chain:
            r_id=residue.get_id()
            h=r_id[0]
            if h=='H_BNZ':
                for atom in residue:
                    a.append(atom)
t=parser.get_structure("5jwt","5jwt.pdb")
for model in t:
    for chain in model:
        for residue in chain:
            R_id=residue.get_id()
            H=R_id[0]
            if H=='H_BNZ':
                for atom in residue:
                    b.append(atom)
print a
print b
from Bio.PDB import Superimposer
sup=Superimposer()
sup.set_atoms(a,b)
for model in t:
    for residue in chain:
        for atom in residue:
            c.append(atom)
sup.apply(c)
for atom in t:
    io=PDBIO()
    io.set_structure(t)
    io.save("5jwt_rotated.pdb")
    
