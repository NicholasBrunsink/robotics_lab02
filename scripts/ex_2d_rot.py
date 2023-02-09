# import the necessary modules
import rbm
import math
import numpy as np

if __name__ == '__main__':
	# define a rotation angle
	theta = math.pi/2
	print('rot_2d function: ', rbm.rot_2d.__doc__)
	print('a %0.2f radian rotation in 2D is shown by'%theta)
	np.set_printoptions(precision=2, suppress=True)
	print(rbm.rot_2d(theta))
