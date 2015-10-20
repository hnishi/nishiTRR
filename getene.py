import struct, sys, os
import numpy as np

single = np.fromfile("128390.fb.ene")
for i in single:
  print i

