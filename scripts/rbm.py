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
	rot = np.array([1,0,0],
					[0,math.cos(theta), -math.sin(theta)]),
				    [0,math.sin(theta), math.cos(theta)])
				  
