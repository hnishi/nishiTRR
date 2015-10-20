#from loadTRR import * 
import loadTRR
import struct, sys, os
import numpy as np

aaa = ['CA','C','N','O']
num_selatom =[]
bbb = []
f_in_pdb = open("npt.gro")
for a in f_in_pdb:
  if len(a.split()) > 8:
    if a.split()[1] in aaa:
      #print a.split()[1],a.split()[2]  
      num_selatom.append(int(a.split()[2]) - 1)

for fl in os.listdir(os.getcwd()):
  if fl[-4:] != ".trr": continue
  #f_in = fl
  f_in = "repair_128390.trr"
  
  f_out = f_in[:-3]+"dist"
  #fp = open(f_out, "wb")
  fp = open(f_out, "w")

  imada_number = 0
  dist = []
  for frame in loadTRR.loadTRR(f_in):
    bbb = []
    #print frame["step"]
    for i in num_selatom:
      #print frame["x"][i],frame["x"][i+1],frame["x"][i+2]
      bbb.append([frame["x"][i],frame["x"][i+1],frame["x"][i+2]])
    ccc = np.array(bbb)
    len_ccc = len(ccc)
    #print len_ccc
    #print (len_ccc * (len_ccc - 1 )) /2
    for m in range(len_ccc):
      for n in range(len_ccc):
        if m < n:
          #print ccc[m],ccc[n]
          #print np.linalg.norm( ccc[m] - ccc[n] )
          print >> fp, np.linalg.norm( ccc[m] - ccc[n] ),",",
          dist.append( np.linalg.norm( ccc[m] - ccc[n] ) )
    #print len(dist)
    print >> fp, ""
    imada_number += 1
    

  fp.close()
#print ccc 
  #print "total frame", imada_number

