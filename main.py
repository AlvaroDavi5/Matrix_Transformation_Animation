"""

	This code has created by Alvaro Davi using STL models avaliable on:
		https://nasa3d.arc.nasa.gov/models



	Segundo Trabalho: Animacao Tridimensional usando Transformacoes Matriciais

	Alvaro Davi S. Alves - 2020101874

	Expressao Grafica para Engenharia

	Universidade Federal do Espirito Santo

"""


''' import libs '''
import matplotlib.pyplot as plt # graphics and math expressions plot
#%matplotlib inline # show plots on jupyter notebook cell
from mpl_toolkits.mplot3d import Axes3D, art3d # class and module to 3D projection
''' import modules '''
from source import stl_models as md # .stl models generated
#import source.animation as anmt # animation functions
import source.transformation as tfmt # transformations matrix



# projection models declarated and initialized
cassini = md.cassini
juno = md.juno


''' plotting the 3D vertices of the triangular faces '''
fig = plt.figure(num=1,figsize=[10,10]) # create fist plot
axes0 = plt.axes(projection='3d')
axes0.plot(md.cassini[0,:],md.cassini[1,:],md.cassini[2,:], 'gold') # plot the points drawing the lines (gold color)
md.set_axes_equal(axes0) # adjust axes

''' plotting another 3D vertices of the triangular faces '''
fig = plt.figure(num=2,figsize=[10,10]) # create fist plot
axes2 = plt.axes(projection='3d')
axes2.plot(md.juno[0,:],md.juno[1,:],md.juno[2,:],'#240f00') # plot the points drawing the lines (brown color)
md.set_axes_equal(axes2) # adjust axes


"""

''' plotting the 3D triangular faces of the object '''
fig = plt.figure(num=2,figsize=[10,10]) # create a new plot
axes1 = plt.axes(projection='3d')
axes1.add_collection3d(art3d.Poly3DCollection(md.juno_vectors, color='#240f00')) # plot and render the faces of the object
axes1.add_collection3d(art3d.Line3DCollection(md.juno_vectors, colors='darkgray', linewidths=0.2, linestyles='-')) # plot the contours of the faces of the object
axes1.plot(md.juno[0,:],md.juno[1,:],md.juno[2,:], 'lightgrey') # plot the vertices of the object
''' set axes and their aspect '''
axes1.auto_scale_xyz(md.juno[0,:],md.juno[1,:],md.juno[2,:])
md.set_axes_equal(axes1)

''' plotting another 3D vertices of the triangular faces '''
fig = plt.figure(num=3,figsize=[10,10]) # create fist plot
axes2 = plt.axes(projection='3d')
axes2.plot(md.rock[0,:],md.rock[1,:],md.rock[2,:],'#3f5946') # plot the points drawing the lines
md.set_axes_equal(axes2) # adjust axes

''' plot all object points '''
figure = plt.figure(num=4)
axes3 = Axes3D(figure)
axes3.add_collection3d(art3d.Poly3DCollection(cassini_stl.vectors))
scale = cassini_stl.points.flatten()
axes3.auto_scale_xyz(scale, scale, scale)

"""


plt.show() # show all figures in a plotting windown
