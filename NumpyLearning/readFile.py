import numpy as np

data = np.genfromtxt('C:/AnsonPython/MyCursorWorks/NumpyLearning/world_alcohol.txt', delimiter=',', dtype=None, names=True)
print(type(data))
print(data)