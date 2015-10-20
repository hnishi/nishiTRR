import os
inpf = "/work1/nkamiya/DATA/ala/mdx-126/"
outf = ""
pcaID = 1
gmx = "/home/nkamiya/gromacs-5.1/build/bin/gmx"
id = [fl for fl in os.listdir(inpf) if fl[-4:] == ".trr"][0].split(".")[0]
cmd = "echo %s | "%pcaID + gmx + " trjconv -f %s.gro -o %s.gro -s %s.tpr"%(inpf+id, outf+id, inpf+id)
os.system(cmd)
cmd = "echo %s | "%pcaID + gmx + " trjconv -f %s.gro -o %s.pdb -s %s.tpr"%(inpf+id, outf+id, inpf+id)
os.system(cmd)
for fl in os.listdir(inpf):
  if fl[-4:] != ".trr": continue
  id = fl.split(".")[0]
  cmd = "echo %s | "%pcaID + gmx + " trjconv -f %s.trr -o %s.trr -s %s.tpr"%(inpf+id, outf+id, inpf+id)
  os.system(cmd)

