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
import matplotlib.pyplot as plt # graphics and math expressions plot
#%matplotlib inline # show plots on jupyter notebook cell
from mpl_toolkits.mplot3d import Axes3D, art3d # class and module to 3D projection
from matplotlib import animation, rc # function and module to plot 3D animation
''' import modules '''
from source import stl_models as md # .stl models generated
import source.transformation as tfmt # transformations matrix



''' function to representing the object in homogeneous coordinates '''
def setObjects(my_object):
	num_columns = np.size(my_object, 1)
	ones_line = np.ones(num_columns) # create row of ones

	my_object = np.vstack([my_object, ones_line]) # add to the object matrix to represent the object in homogeneous coordinatess

	return my_object


''' declared and initialized objects '''
cassini = setObjects(md.cassini)
juno = setObjects(md.juno)



fig = plt.figure(figsize=(10,10))
ax0 = plt.axes(projection='3d')
#plt.close()

ax0.set_xlim3d((-50, 50))
ax0.set_ylim3d((-50, 50))
ax0.set_zlim3d((-10, 50))

''' listing the objects that are going to be drawn '''
obj1, = ax0.plot3D([], [], [], lw=2, color='gold')
obj2, = ax0.plot3D([], [], [], lw=2,  color='#240f00')  


''' animation initialization function '''
def init():
	obj1.set_data(cassini[0,:], cassini[1,:])
	obj1.set_3d_properties(cassini[2,:])
	return (obj1,)

''' animation function, is called sequentially '''
def animate(i):
	# Defining the translation to be applied to a second object
	T3 = tfmt.move(-0.05*i,0.3*i,0.2*i)
	# Move the object
	my_obj1 = np.dot(T3, juno)

	obj2.set_data(my_obj1[0,:], my_obj1[1,:])
	obj2.set_3d_properties(my_obj1[2,:])

	return (obj2,)


anim = animation.FuncAnimation(fig, func=animate, init_func=init, frames=100, interval=100, blit=True) # make the animation

''' this part which makes it work on Colab '''
#rc('animation', html='jshtml')
#anim

plt.show()

"""

''' plotting the 3D vertices of the triangular faces '''
fig = plt.figure(num=1,figsize=[10,10]) # create fist plot
axes0 = plt.axes(projection='3d')
axes0.plot(cassini[0,:],cassini[1,:],cassini[2,:], 'gold') # plot the points drawing the lines (gold color)
md.set_axes_equal(axes0) # adjust axes


''' plotting the 3D triangular faces of the object '''
fig = plt.figure(num=2,figsize=[10,10]) # create a new plot
axes1 = plt.axes(projection='3d')
axes1.add_collection3d(art3d.Poly3DCollection(md.juno_vectors, color='#240f00')) # plot and render the faces of the object
axes1.add_collection3d(art3d.Line3DCollection(md.juno_vectors, colors='darkgray', linewidths=0.2, linestyles='-')) # plot the contours of the faces of the object
axes1.plot(juno[0,:],juno[1,:],juno[2,:], 'lightgrey') # plot the vertices of the object
''' set axes and their aspect '''
axes1.auto_scale_xyz(juno[0,:],juno[1,:],juno[2,:])
md.set_axes_equal(axes1)


''' plot all object points '''
figure = plt.figure(num=3,figsize=[10,10])
axes3 = Axes3D(figure)
axes3.add_collection3d(art3d.Poly3DCollection(md.cassini_vectors))
scale = md.cassini_stl.points.flatten()
axes3.auto_scale_xyz(scale, scale, scale)


plt.show() # show all figures in a plotting windown

"""

