
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D, art3d # class and module to 3D projection
from matplotlib import animation, rc # function and module to plot 3D animation
import source.transformation as tfmt
import source.stl_models as md



''' representing the object in homogeneous coordinates '''
house = tfmt.house
house = np.transpose(house)
num_columns = np.size(house, 1)
ones_line = np.ones(num_columns) # create row of ones

house = np.vstack([house, ones_line]) # add to the house matrix to represent the house in homogeneous coordinatess

fig = plt.figure(figsize=(10,10))
ax0 = plt.axes(projection='3d')
plt.close()

ax0.set_xlim3d((-50, 50))
ax0.set_ylim3d((-50, 50))
ax0.set_zlim3d((-10, 50))

obj1, = ax0.plot3D([], [], [], lw=2,color='#4004B0') # listing the objects that are going to be drawn
obj2, = ax0.plot3D([], [], [], '--', lw=2)  


# initialization function: 
def init():
	obj1.set_data(house[0,:], house[1,:])
	obj1.set_3d_properties(house[2,:])
	return (obj1,)

# animation function. This is called sequentially
def animate(i):
	# Defining the translation to be applied to a second object
	T3 = tfmt.move(-0.05*i,0.3*i,0.2*i)
	# Move the object
	house2 = np.dot(T3, house)

	obj2.set_data(house2[0,:], house2[1,:])
	obj2.set_3d_properties(house2[2,:])

	return (obj2,)

# Make the animation
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=100, blit=True)

# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')
anim
