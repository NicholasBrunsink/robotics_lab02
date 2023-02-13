# Here we write some functions that help us analyze the motions of a rigid body
# import math module and numpy module
import math
import numpy as np

# define a 2d rotation matrix
def rot_2d(theta):
	'''
	This function recieves an input in radians
	and returns  2d rotation matrix
	R = | cos(theta)  -sin(theta) |
		| sin(theta)  cos(theta)  |
	'''
	rot = np.array([ [math.cos(theta), -math.sin(theta)], 
					 [math.sin(theta), math.cos(theta)] ])
	return rot
	
def rot_x(theta):
	'''
	This function recieves an input in radians
	and returns a 3d rotation matrix in the x direction
	R = | 1			  0			  0 |
		| cos(theta) -sin(theta)  0 |
		| sin(theta)  cos(theta)  0 |
	'''
	rot = np.array([
		[1.0,  0.0, 0.0],
		[0.0, math.cos(theta), -math.sin(theta)],
		[0.0, math.sin(theta), math.cos(theta)]])
	return rot

def rot_y(theta):
	'''
	This function recieves an input in radians
	and returns a 3d rotation matrix in the y direction
	R = | cos(theta)   0   sin(theta) |
		| 0			   1			0 |
		| -sin(theta)  0   cos(theta) |
	'''
	rot = np.array([
		[math.cos(theta),  0.0, math.sin(theta)],
		[0.0, 1.0, 0.0],
		[-math.sin(theta), 0.0, math.cos(theta)]])
	return rot

def rot_z(theta):
	'''
	This function recieves an input in radians
	and returns a 3d rotation matrix in the z direction
	R = | cos(theta) -sin(theta)  0 |
		| sin(theta)  cos(theta)  0 |
		| 0			  0			  1 |
	'''
	rot = np.array([
		[math.cos(theta),  -math.sin(theta), 0.0],
		[math.sin(theta),   math.cos(theta), 0.0],
		[0.0, 0.0, 1.0]])
	rot = np.around(rot,decimals=2)
	return rot

def vec(x,y,z):
	# Create a vector using a numpy array 
	# and transpose it into a column vector
	vec = np.array([[x,y,z]]).T
	return vec