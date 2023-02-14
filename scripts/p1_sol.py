# Importing rbm created in class
import rbm
# importing math and numpy to support matrix operation and trig functionality
import math
import numpy as np

if __name__ == '__main__':
    # Setting print options
    np.set_printoptions(precision = 2, suppress = True)

    # Setting rotation angles for x, y, and z
    psi = math.pi/2
    theta = math.pi/2
    phi = math.pi/2

    # creating vector to test rotation
    V = np.array([1,1,1])

    print(f'\Pre Roll-Pitch-Yaw Vector:\n {V}\n')

    # generating rotation matrix for x direction using psi
    Rx = rbm.rot_x(psi)
    # generating rotation matrix for y direction using theta
    Ry = rbm.rot_y(theta)
    # generating rotation matrix for z direction using phi
    Rz = rbm.rot_z(phi)

    # Multiplying rotation matricies using fixed frame RzRyRx    
    Rzy = np.matmul(Rz, Ry)
    Rzyx = np.matmul(Rzy, Rx)

    # Applying rotation matrix to test vector
    finalVec = np.matmul(V, Rzyx)

    # Printing results
    print(f'Post Roll-Pitch-Yaw Rotation Matrix:\n{Rzyx}')
    print(f'\nPost Roll-Pitch-Yaw Vector:\n {finalVec}')