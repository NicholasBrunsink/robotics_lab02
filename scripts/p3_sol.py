# import p2_sol to create transformation matricies from the formulas made in p2
import p2_sol as p2
# import numpy and math to support needed matrix and trig functions
import numpy as np
import math

if __name__ == "__main__":
    np.set_printoptions(precision = 2, suppress = True)
    # Create a vector to test transformations on
    test = np.array([1, 1, 1, 1])

    # Homogeneous transformation of a translation of
    #                               2.5 in the x direction, 
    #                               0.5 in the z direction,
    #                          and -1.5 in the y direction
    #                               using the current frame
    H_1 = np.matmul(
            np.matmul(
                p2.xTranslate(2.5), 
                p2.zTranslate(0.5)), 
                p2.yTranslate(-1.5))
    print(H_1)
    print()

    # Homogeneous transformation of a translation of
    #                               0.5 in the z direction,
    #                               2.5 in the x direction,              
    #                          and -1.5 in the y direction
    #                               using the current frame
    H_2 = np.matmul(
            np.matmul(
                p2.zTranslate(0.5), 
                p2.xTranslate(2.5)), 
                p2.yTranslate(-1.5))
    print(H_2)
    print()

    # Homogeneous transformation of a translation of
    #                               2.5 in the x direction, 
    #                               0.5 in the z direction,
    #                          and -1.5 in the y direction
    #                               using the fixed frame
    H_3 = np.matmul(
            np.matmul(
                p2.yTranslate(-1.5),
                p2.zTranslate(0.5)), 
                p2.xTranslate(2.5))
    print(H_3)
    print()

    # Homogeneous transformation of a translation of 
    #                               0.5 in the z direction,
    #                               2.5 in the x direction,              
    #                          and -1.5 in the y direction
    #                               using the fixed frame
    H_4 = np.matmul(
            np.matmul(
                p2.yTranslate(-1.5),
                p2.xTranslate(2.5)), 
                p2.zTranslate(0.5)) 
    print(H_4) 
    print()  

    # Homogenous transformation of a
    #                       rotation of pi/2 about the current x-axis
    #                       translation of 3 units along the current x-axis
    #                       translation of -3 units along the current z-axis
    #                       rotation of -pi/2 about the current z-axis
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