import numpy as np

# Create a 2D Numpy array list of list
arr2D = np.array([[11, 12, 13, 22], [21, 7, 23, 14], [31, 10, 33, 7]])
# Save 2D numpy array to csv file
np.savetxt('2darray.csv', arr2D, delimiter=',', fmt='%d')