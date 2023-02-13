import rbm
import math
import numpy as np

if __name__ == '__main__':
	# Define a rotation angle
	theta = math.pi/2

	# Update the output format
	np.printoptions(precision = 2, suppress=True)

	# Define the v0 vector
	v0 = rbm.vec(1,1,1)
	print(v0)
	print()

	# Generating rotation matricies
	Ry = rbm.rot_y(theta)
	Rx = rbm.rot_x(theta)
	Rz = rbm.rot_z(theta)

	v01 = Rx.dot(v0)
	v12 = Ry.dot(v01)
	v23 = Rz.dot(v12)

	print(v23)