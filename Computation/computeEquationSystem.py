import numpy as np

A = np.array([[2,-1],[1,1]]) 
b = np.array([1,5]) 
print(np.linalg.solve(A,b))