
import struct, sys, os
import numpy as np


def getFloatSize(header):
  DIM = 3
  floatSize = 0
  if header.has_key("box_size"): floatSize = header["box_size"]/(DIM*DIM)
  elif header.has_key("x_size"): floatSize = header["x_size"]/(header["natoms"]*DIM)
  elif header.has_key("v_size"): floatSize = header["v_size"]/(header["natoms"]*DIM)
  elif header.has_key("f_size"): floatSize = header["f_size"]/(header["natoms"]*DIM)
  else: print "WARNING: Unknown precision of TRR file..."
  return floatSize

def loadTRR(fl):
  fp = open(fl)
  
  while True:
    chunk = fp.read(12)
    if chunk == "": break
  
    frame = {}
    
    frame["magicnum"], frame["i1"], version_sz = struct.unpack(">iiI", chunk)
    
    frame["version"] = "".join(struct.unpack(">" + "c"*version_sz, fp.read(version_sz)))
    frame["ir_size"], frame["e_size"], frame["box_size"], frame["vir_size"], frame["pres_size"], frame["top_size"], frame["sym_size"], frame["x_size"], frame["v_size"], frame["f_size"], frame["natoms"], frame["step"], frame["nre"] = struct.unpack(">iiiiiiiiiiiii", fp.read(13*4))
  
    floatSize = getFloatSize(frame)
    if floatSize == 8: floatSymbol = "d"
    else: floatSymbol = "f"

    frame["time"], frame["lam"] = struct.unpack(">"+floatSymbol+floatSymbol, fp.read(floatSize*2))

  
    if frame["box_size"]:
      vector = frame["box"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["box_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)
    
    if frame["vir_size"]:
      vector = frame["vir"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["vir_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)
    
    if frame["pres_size"]:
      vector = frame["pres"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["vir_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)    
  
    if frame["x_size"]:
      vector = frame["x"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["x_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)
    
    if frame["v_size"]:
      vector = frame["v"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["v_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)
    
    if frame["f_size"]:
      vector = frame["f"] = np.fromfile(fp, dtype=">"+floatSymbol, count=frame["f_size"]/floatSize)
      vector = vector.reshape(len(vector)/3, 3)

    yield frame

"""
for fl in os.listdir(os.getcwd()):
  if fl[-4:] != ".trr": continue
  f_in = fl
  

  f_out = f_in[:-3]+"gcod"

  # frame number
  # box size
  # x

  fp = open(f_out, "wb")

  for frame in loadTRR(f_in):
    print frame["step"]
    fp.write(struct.pack("i", frame["step"]))
    frame["box"].flatten().astype(np.float32).tofile(fp)
    frame["x"].flatten().astype(np.float32).tofile(fp)
  
  fp.close()
"""

