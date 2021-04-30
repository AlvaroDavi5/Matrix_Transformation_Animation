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



#first plot
figure = plt.figure()
axes = Axes3D(figure)
cassini = mesh.Mesh.from_file("./models/cassini.stl")
juno = mesh.Mesh.from_file("./models/Juno.stl")
rock_ground = mesh.Mesh.from_file("./models/Block_Island.stl")
axes.add_collection3d(art3d.Poly3DCollection(juno.vectors))
scale = juno.points.flatten()
axes.auto_scale_xyz(scale, scale, scale)


# -----------------------------------------------------------------------------------------------------------------

# Complementary function to make the 3D axes aspect equal 

def set_axes_equal(ax):
    #Make axes of 3D plot have equal scale so that spheres appear as spheres,
    #cubes as cubes, etc..  This is one possible solution to Matplotlib's
    #ax.set_aspect('equal') and ax.axis('equal') not working for 3D.

    #Input
    #  ax: a matplotlib axis, e.g., as output from plt.gca().
    
    x_limits = ax.get_xlim3d()
    y_limits = ax.get_ylim3d()
    z_limits = ax.get_zlim3d()

    x_range = abs(x_limits[1] - x_limits[0])
    x_middle = np.mean(x_limits)
    y_range = abs(y_limits[1] - y_limits[0])
    y_middle = np.mean(y_limits)
    z_range = abs(z_limits[1] - z_limits[0])
    z_middle = np.mean(z_limits)

    # The plot bounding box is a sphere in the sense of the infinity
    # norm, hence I call half the max range the plot radius.
    plot_radius = 0.5*max([x_range, y_range, z_range])

    ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
    ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
    ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])




# Load the STL files and add the vectors to the plot
your_mesh = mesh.Mesh.from_file('./models/Juno.stl')

# Get the x, y, z coordinates contained in the mesh structure that are the 
# vertices of the triangular faces of the object
x = your_mesh.x.flatten()
y = your_mesh.y.flatten()
z = your_mesh.z.flatten()

# Get the vectors that define the triangular faces that form the 3D object
kong_vectors = your_mesh.vectors

# Create the 3D object from the x,y,z coordinates and add the additional array of ones to 
# represent the object using homogeneous coordinates
kong = np.array([x.T,y.T,z.T,np.ones(x.size)])

#print(kong.shape)

###################################################
# Plotting the 3D vertices of the triangular faces
###################################################

# Create a new plot
fig = plt.figure(1,figsize=[10,10])
axes0 = plt.axes(projection='3d')

# Plot the points drawing the lines
axes0.plot(kong[0,:],kong[1,:],kong[2,:],'r')
set_axes_equal(axes0)




###################################################
# Plotting the 3D triangular faces of the object
###################################################

# Create a new plot
fig = plt.figure(2,figsize=[10,10])
axes1 = plt.axes(projection='3d')

# Plot and render the faces of the object
axes1.add_collection3d(art3d.Poly3DCollection(kong_vectors))
# Plot the contours of the faces of the object
axes1.add_collection3d(art3d.Line3DCollection(kong_vectors, colors='k', linewidths=0.2, linestyles='-'))
# Plot the vertices of the object
axes1.plot(kong[0,:],kong[1,:],kong[2,:],'k.')

# Set axes and their aspect
axes1.auto_scale_xyz(kong[0,:],kong[1,:],kong[2,:])
set_axes_equal(axes1)
# Show the plots 
plt.show()
