import p2_sol as p2
import numpy as np
import math

if __name__ == "__main__":
    np.set_printoptions(precision = 2, suppress = True)
    test = np.array([1, 1, 1, 1])
    H_1 = np.matmul(
            np.matmul(
                p2.xTranslate(2.5), 
                p2.zTranslate(0.5)), 
                p2.yTranslate(-1.5))
    print(np.matmul(test, H_1))

    H_2 = np.matmul(
            np.matmul(
                p2.zTranslate(0.5), 
                p2.xTranslate(2.5)), 
                p2.yTranslate(-1.5))
    print(np.matmul(test, H_2))

    H_3 = np.matmul(
            np.matmul(
                p2.yTranslate(-1.5),
                p2.zTranslate(0.5)), 
                p2.xTranslate(2.5))
    print(np.matmul(test, H_3))

    H_4 = np.matmul(
            np.matmul(
                p2.yTranslate(-1.5),
                p2.xTranslate(2.5)), 
                p2.zTranslate(0.5)) 
    print(H_4)   
    print(np.matmul(test, H_4))

    theta = math.pi/2
    H_5 = np.matmul(
            np.matmul(
            np.matmul(
                p2.xRotate(theta),
                p2.xTranslate(3)),
                p2.zTranslate(-3)),
                p2.zRotate(-theta)
            )
    print(H_5)
    print(np.matmul(test,H_5))