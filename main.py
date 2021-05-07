"""

	This code has created by Alvaro Davi using STL models avaliable on:
		https://nasa3d.arc.nasa.gov/models



	Segundo Trabalho: Animacao Tridimensional usando Transformacoes Matriciais

	Alvaro Davi S. Alves - 2020101874

	Expressao Grafica para Engenharia Eletrica

	Universidade Federal do Espirito Santo

"""


''' import libs '''
from scipy.constants import pi # scientific functions and numerics constants
import numpy as np # numeric manipulations, constants and functions
import matplotlib.pyplot as plt # graphics and math expressions plot
#%matplotlib inline # show plots on jupyter notebook cell
from mpl_toolkits.mplot3d import Axes3D, art3d # class and module to 3D projection
from matplotlib.animation import FuncAnimation # function to plot 3D animation
from matplotlib import rc # function and module to plot 3D animation
''' import modules '''
import source.stl_models as md # .stl models generated
from source import transformation as tfmt # transformations matrix



''' function to representing the object in homogeneous coordinates '''
def setObjects(my_object):
	num_columns = np.size(my_object, 1)
	ones_line = np.ones(num_columns) # create row of ones

	my_object = np.vstack([my_object, ones_line]) # add to the object matrix to represent the object in homogeneous coordinatess

	return my_object


''' declared and initialized objects '''
cassini = setObjects(md.cassini)
juno = setObjects(md.juno)


''' creating the figure to animation '''
fig = plt.figure(num=0, figsize=(10,10))
ax0 = plt.axes(projection='3d')

''' limiting the plot axis size '''
ax0.set_xlim3d((-90, 90))
ax0.set_ylim3d((-90, 90))
ax0.set_zlim3d((-90, 90))
ax0.set_title("Collision between Juno and Cassini probes")
ax0.set_xlabel("X Axis")
ax0.set_ylabel("Y Axis")
ax0.set_zlabel("Z Axis")

''' listing the objects that are going to be drawn '''
obj1, = ax0.plot3D([], [], [], lw=2, color='gold')
obj2, = ax0.plot3D([], [], [], lw=2,  color='#240f00')  


''' animation function, is called sequentially '''
def init():
	# defining the objects
	my_obj1 = cassini
	my_obj2 = juno

	# set objects
	obj1.set_data(my_obj1[0,:], my_obj1[1,:])
	obj1.set_3d_properties(my_obj1[2,:])
	obj2.set_data(my_obj2[0,:], my_obj2[1,:])
	obj2.set_3d_properties(my_obj2[2,:])

	return (obj1, obj2,)

''' animation function, is called sequentially '''
def animate(i):
	# defining the transformation to animation
	rotate_slowly = tfmt.y_rotation((pi/2)*0.01*i)
	rotate_quickly = tfmt.x_rotation((pi/2)*0.09*i)
	result_curve = tfmt.y_rotation((pi/2)*0.03*i)
	result_traject = tfmt.move(-60+0.6*i, -60+0.5*i, -60+0.6*i) # after the crash, cassini will have its trajectory deflected
	normal_traject = tfmt.move(-60+0.5*i, -60+0.4*i, -60+0.5*i) # going from (-60, -60, -60) to (40, 20, 40)
	move_reflected = np.dot(-1, normal_traject) # by the contrary force, the trajectory is made in the original direction

	# moving the objects
	if i < 120:
		my_obj1 = np.dot(rotate_slowly, cassini)
		my_obj2 = np.dot(normal_traject, juno)
	else:
		my_obj1 = np.dot(np.dot(result_traject, rotate_quickly), cassini)
		my_obj2 = np.dot(np.dot(move_reflected, result_curve), juno)

	# set objects
	obj1.set_data(my_obj1[0,:], my_obj1[1,:])
	obj1.set_3d_properties(my_obj1[2,:])
	obj2.set_data(my_obj2[0,:], my_obj2[1,:])
	obj2.set_3d_properties(my_obj2[2,:])

	return (obj1, obj2,)


anim = FuncAnimation(fig, func=animate, init_func=init, frames=200, interval=50, blit=True) # make the animation

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

