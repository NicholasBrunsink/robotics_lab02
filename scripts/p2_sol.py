import math
import numpy as np

def xTranslate(a):
    translate = np.array([
		[1, 0, 0, a],
		[0, 1, 0, 0],
		[0, 0, 1, 0],
        [0, 0, 0, 1]])
    return translate

def yTranslate(b):
    translate = np.array([
		[1, 0, 0, 0],
		[0, 1, 0, b],
		[0, 0, 1, 0],
        [0, 0, 0, 1]])
    return translate

def zTranslate(c):
    translate = np.array([
		[1, 0, 0, 0],
		[0, 1, 0, 0],
		[0, 0, 1, c],
        [0, 0, 0, 1]])
    return translate

def xRotate(alpha):
    rotate = np.array([
		[1,     0,                  0,                  0],
		[0,     math.cos(alpha),   -math.sin(alpha),    0],
		[0,     math.sin(alpha),    math.cos(alpha),    0],
        [0,     0,                  0,                  1]])
    return rotate

def yRotate(alpha):
    rotate = np.array([
		[math.cos(alpha),   0,  -math.sin(alpha), 0],
		[0,                 1,   0,               0],
		[math.sin(alpha),   0,   math.cos(alpha), 0],
        [0,                 0,   0,               1]])
    return rotate

def zRotate(alpha):
    rotate = np.array([
		[math.cos(alpha),  -math.sin(alpha),    0,  0],
		[math.sin(alpha),   math.cos(alpha),    0,  0],
		[0,                 0,                  1,  0],
        [0,                 0,                  0,  1]])
    return rotate