"""

This code has created by Alvaro Davi using STL models avaliable on:
	https://nasa3d.arc.nasa.gov/models



Segundo Trabalho: Animacao Tridimensional usando Transformacoes Matriciais

Alvaro Davi S. Alves - 2020101874

Expressao Grafica para Engenharia

Universidade Federal do Espirito Santo

"""


''' import libs '''
import numpy as np # numeric manipulations, constants and functions
 # scientific methods and functions
import matplotlib.pyplot as plt # graphics and math expressions plot
#%matplotlib inline # show plots on jupyter notebook line
from mpl_toolkits.mplot3d import Axes3D, art3d # class and module to 3D projection
from math import sin, cos, tan # trigonometric functions
from stl import mesh # .stl files read



figure = plt.figure()
axes = Axes3D(figure)
cassini = mesh.Mesh.from_file("./models/cassini.stl")
juno = mesh.Mesh.from_file("./models/Juno.stl")
rock_ground = mesh.Mesh.from_file("./models/Block_Island.stl")
axes.add_collection3d(art3d.Poly3DCollection(cassini.vectors))
scale = cassini.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)
plt.show()
