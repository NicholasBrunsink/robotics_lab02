import math
import numpy as np

def xTranslate(a):
    '''
	This function recieves an input for translation distance
	and returns a 3d translation matrix in the x direction
	R = | 1	 0  0  a |
		| 0  1  0  0 |
		| 0  0  1  0 |
        | 0  0  0  1 |
	'''
    translate = np.array([
		[1, 0, 0, a],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
        [0, 0, 0, 1]])
    return translate

def yTranslate(b):
    '''
	This function recieves an input for translation distance
	and returns a 3d translation matrix in the y direction
	R = | 1	 0  0  0 |
		| 0  1  0  b |
		| 0  0  1  0 |
        | 0  0  0  1 |
	'''
    translate = np.array([
		[1, 0, 0, 0],
		[0, 1, 0, b],
		[0, 0, 1, 0],
        [0, 0, 0, 1]])
    return translate

def zTranslate(c):
    '''
	This function recieves an input for translation distance
	and returns a 3d translation matrix in the z direction
	R = | 1	 0  0  0 |
		| 0  1  0  0 |
		| 0  0  1  c |
        | 0  0  0  1 |
	'''
    translate = np.array([
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, c],
        [0, 0, 0, 1]])
    return translate

def xRotate(alpha):
    '''
	This function recieves an input in radiams
	and returns a 3d rotation matrix in the x direction
	R = | 1	    0               0            0 |
		| 0     cos(alpha)     -sin(alpha)   0 |
		| 0     sin(alpha)      cos(alpha)   0 |
        | 0     0               0            1 |
	'''
    rotate = np.array([
		[1,     0,                  0,                  0],
		[0,     math.cos(alpha),   -math.sin(alpha),    0],
		[0,     math.sin(alpha),    math.cos(alpha),    0],
        [0,     0,                  0,                  1]])
    return rotate

def yRotate(alpha):
    '''
	This function recieves an input in radiams
	and returns a 3d rotation matrix in the y direction
	R = | cos(alpha)    0      -sin(alpha)      0 |
		| 0             1       0               0 |
		| sin(alpha)    0       cos(alpha)      0 |
        | 0             0       0               1 |
	'''
    rotate = np.array([
		[math.cos(alpha),   0,  -math.sin(alpha), 0],
		[0,                 1,   0,               0],
		[math.sin(alpha),   0,   math.cos(alpha), 0],
        [0,                 0,   0,               1]])
    return rotate

def zRotate(alpha):
    '''
	This function recieves an input in radians
	and returns a 3d rotation matrix in the z direction
	R = | cos(alpha)    -sin(alpha)     0       0 |
		| sin(alpha)    cos(alpha)      0       0 |
		| 0             0               1       0 |
        | 0             0               0       1 |
	'''
    rotate = np.array([
		[math.cos(alpha),  -math.sin(alpha),    0,  0],
		[math.sin(alpha),   math.cos(alpha),    0,  0],
		[0,                 0,                  1,  0],
        [0,                 0,                  0,  1]])
    return rotate