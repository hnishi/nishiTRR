#from loadTRR import * 
import loadTRR
import struct, sys, os
import numpy as np

atomname = ['CA','C','N','O']
num_selatom =[]
coord = []
f_in_pdb = open("npt.gro")
for a in f_in_pdb:
  if len(a.split()) > 8:
    if a.split()[1] in atomname:
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
    coord = []
    #print frame["step"]
    for i in num_selatom:
      #print frame["x"][i],frame["x"][i+1],frame["x"][i+2]
      coord.append([frame["x"][i],frame["x"][i+1],frame["x"][i+2]])
    coord_array = np.array(coord)
    len_coord_array = len(coord_array)
    #print len_coord_array
    #print (len_coord_array * (len_coord_array - 1 )) /2
    for m in range(len_coord_array):
      for n in range(len_coord_array):
        if m < n:
          #print coord_array[m],coord_array[n]
          #print np.linalg.norm( coord_array[m] - coord_array[n] )
          print >> fp, np.linalg.norm( coord_array[m] - coord_array[n] ),",",
          dist.append( np.linalg.norm( coord_array[m] - coord_array[n] ) )
    #print len(dist)
    print >> fp, ""
    imada_number += 1
    

  fp.close()
print frame["box"]
#print coord_array 
  #print "total frame", imada_number

