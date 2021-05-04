
from stl import mesh # .stl files read
import numpy as np # numeric manipulations, constants and functions



''' load the STL files and add the vectors to the plot '''
cassini_stl = mesh.Mesh.from_file("./models/cassini.stl")
juno_stl = mesh.Mesh.from_file("./models/Juno.stl")


''' make axes of 3D plot have equal scale so that spheres appear as spheres, cubes as cubes, etc..  This is one possible solution to Matplotlib's ax.set_aspect('equal') and ax.axis('equal') not working for 3D '''
def set_axes_equal(ax): # 'ax' is a matplotlib axis, e.g., as output from plt.gca()

	x_limits = ax.get_xlim3d()
	y_limits = ax.get_ylim3d()
	z_limits = ax.get_zlim3d()

	x_range = abs(x_limits[1] - x_limits[0])
	x_middle = np.mean(x_limits)
	y_range = abs(y_limits[1] - y_limits[0])
	y_middle = np.mean(y_limits)
	z_range = abs(z_limits[1] - z_limits[0])
	z_middle = np.mean(z_limits)

	plot_radius = 0.5*max([x_range, y_range, z_range]) # the plot bounding box is a sphere in the sense of the infinity norm, hence I call half the max range the plot radius

	ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
	ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
	ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])


''' get the mesh object x, y, z coordinates contained in the mesh structure - readed from STL - that are the vertices of the triangular faces of the object '''
def get3DCoordinatesArray(my_mesh_stl):
	x = my_mesh_stl.x.flatten()
	y = my_mesh_stl.y.flatten()
	z = my_mesh_stl.z.flatten()

	''' create the 3D objects from the x,y,z coordinates and add the additional array of ones to represent the object using homogeneous coordinates '''
	my_mesh = np.array([x.T, y.T, z.T, np.ones(x.size)])  # transposed to become a column

	return my_mesh


''' get the models x, y, z coordinates array '''
cassini = get3DCoordinatesArray(cassini_stl)
juno = get3DCoordinatesArray(juno_stl)

''' get the vectors that define the triangular faces that form the 3D object '''
cassini_vectors = cassini_stl.vectors
juno_vectors = juno_stl.vectors




# creating a house
house_matrix = np.array([
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

house = np.transpose(house_matrix)
