
import matplotlib.pyplot as plt
from scipy.constants import pi # scientific functions and numerics constants
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
def z_rotation(angle):
	rotation_matrix=np.array([[cos(angle),-sin(angle),0,0],[sin(angle),cos(angle),0,0],[0,0,1,0],[0,0,0,1]])
	return rotation_matrix

def y_rotation(angle):
	rotation_matrix=np.array([[cos(angle),0,sin(angle),0],[0,1,0,0],[-sin(angle),0,cos(angle),0],[0,0,0,1]])
	return rotation_matrix

def x_rotation(angle):
	rotation_matrix=np.array([[1,0,0,0],[0, cos(angle),-sin(angle),0],[0, sin(angle),cos(angle),0],[0,0,0,1]])
	return rotation_matrix

''' function to build translation matrix in the axes '''
def move(dx,dy,dz):
	translation = np.array([dx, dy, dx, 1])
	T_matrix = np.eye(4) # create a identity matrix
	T_matrix[:,-1] = translation.T # add [dx,dy,dx,1] in the last column (arrray transposed)
	return T_matrix


# creating a house
house = np.array([
         [0,         0,         0],
         [0,  -10.0000,         0],
         [0, -10.0000,   12.0000],
         [0,  -10.4000,   11.5000],
         [0,   -5.0000,   16.0000],
         [0,         0,   12.0000],
         [0,    0.5000,   11.4000],
         [0,         0,   12.0000],
         [0,         0,         0],
  [-12.0000,         0,         0],
  [-12.0000,   -5.0000,         0],
  [-12.0000,  -10.0000,         0],
         [0,  -10.0000,         0],
         [0,  -10.0000,   12.0000],
  [-12.0000,  -10.0000,   12.0000],
  [-12.0000,         0,   12.0000],
         [0,         0,   12.0000],
         [0,  -10.0000,   12.0000],
         [0,  -10.5000,   11.4000],
  [-12.0000,  -10.5000,   11.4000],
  [-12.0000,  -10.0000,   12.0000],
  [-12.0000,   -5.0000,   16.0000],
         [0,   -5.0000,   16.0000],
         [0,    0.5000,   11.4000],
  [-12.0000,    0.5000,   11.4000],
  [-12.0000,         0,   12.0000],
  [-12.0000,   -5.0000,   16.0000],
  [-12.0000,  -10.0000,   12.0000],
  [-12.0000,  -10.0000,         0],
  [-12.0000,   -5.0000,         0],
  [-12.0000,         0,         0],
  [-12.0000,         0,   12.0000],
  [-12.0000,         0,         0]])

