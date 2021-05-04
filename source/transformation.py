
import matplotlib.pyplot as plt
from math import sin, cos, tan # trigonometric functions
from mpl_toolkits.mplot3d import Axes3D  
# %matplotlib inline
import numpy as np



''' base vector values '''
e1 = np.array([1,0,0]) # X
e2 = np.array([0,1,0]) # Y
e3 = np.array([0,0,1]) # Z
base = [e1,e2,e3] # 3x3
origin_point = np.array([0.0,0.0,0.0,1.0])


''' functions to build rotation matrix around the axes '''
def x_rotation(angle):
	rotation_matrix = np.eye(5) # create a identity matrix
	rotation_matrix[1,1] = cos(angle)
	rotation_matrix[1,2] = -sin(angle)
	rotation_matrix[2,1] = sin(angle)
	rotation_matrix[2,2] = cos(angle)
	return rotation_matrix

def y_rotation(angle):
	rotation_matrix = np.eye(5)
	rotation_matrix[0,0] = cos(angle)
	rotation_matrix[0,2] = sin(angle)
	rotation_matrix[2,0] = -sin(angle)
	rotation_matrix[2,2] = cos(angle)
	return rotation_matrix

def z_rotation(angle):
	rotation_matrix = np.eye(5)
	rotation_matrix[0,0] = cos(angle)
	rotation_matrix[0,1] = -sin(angle)
	rotation_matrix[1,0] = sin(angle)
	rotation_matrix[1,1] = cos(angle)
	return rotation_matrix

''' function to build translation matrix in the axes '''
def move(dx,dy,dz):
	translation = np.array([dx, dy, dx, 1, 1])
	T_matrix = np.eye(5) # create a identity matrix
	T_matrix[:,-1] = translation.T # add [dx,dy,dx,1,1] in the last column (arrray transposed)
	return T_matrix
