import numpy as np

#Define the matrix
A = np.array([[2,-1],[1,1]])
#Define the result vector 
b = np.array([1,5]) 
#Solve the linear equation system
print(np.linalg.solve(A,b))