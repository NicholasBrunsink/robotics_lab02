import rbm
import math
import numpy as np

if __name__ == '__main__':
    np.set_printoptions(precision = 2, suppress = True)

    psi = math.pi/2
    theta = math.pi/2
    phi = math.pi/2

    V = np.array([1,1,1])

    Rx = rbm.rot_x(psi)
    Ry = rbm.rot_y(theta)
    Rz = rbm.rot_z(phi)
    
    Rzy = np.matmul(Rz, Ry)
    Rzyx = np.matmul(Rzy, Rx)

    print(f'Post Roll-Pitch-Yaw Rotation Matrix:\n{Rzyx}')

    print(np.matmul(V, Rzyx))