import sklearn.decomposition
import numpy as np
dim = 4
#data = np.loadtxt("128390.dist",delimiter=",")
data = np.loadtxt("repair_128390.dist",delimiter=",")
print data
pca = sklearn.decomposition.PCA(dim)
result=pca.fit_transform(data)
np.savetxt('result.csv',result,delimiter="   ")
