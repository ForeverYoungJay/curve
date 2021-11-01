#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import math
import matplotlib.pyplot as plt


def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6


def rotationMatrixToEulerAngles(R):
    #assert (isRotationMatrix(R))

    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])

    singular = sy < 1e-6

    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0

    return np.array([x, y, z])


def eulerAnglesToRotationMatrix(theta):
    R_x = np.array([[1, 0, 0],
                    [0, math.cos(theta[0]), -math.sin(theta[0])],
                    [0, math.sin(theta[0]), math.cos(theta[0])]
                    ])

    R_y = np.array([[math.cos(theta[1]), 0, math.sin(theta[1])],
                    [0, 1, 0],
                    [-math.sin(theta[1]), 0, math.cos(theta[1])]
                    ])

    R_z = np.array([[math.cos(theta[2]), -math.sin(theta[2]), 0],
                    [math.sin(theta[2]), math.cos(theta[2]), 0],
                    [0, 0, 1]
                    ])

    R = np.dot(R_z, np.dot(R_y, R_x))

    return R




def getRMfromdirection(RD, ND):
    # 构建点
    TD = np.cross(RD, ND)
    # 计算叉乘
    RD = np.array(RD)
    ND = np.array(ND)
    RM = np.array([RD, TD, ND]).T
    sum =np.linalg.det(RM)

    return RM


if __name__ == '__main__':


    R= getRMfromdirection([-1,2,3],[1,-1,1])
    e = rotationMatrixToEulerAngles(R)

    print(R)
    """for i in range(len(e)):
        if e[i]>2:
            e[i]-=2
    e*=360

    slip=[([0,1,-1],[1,1,1]),([-1,0,1],[1,1,1]),
          ([1,-1,0],[1,1,1]),([0,-1,-1],[-1,-1,1]),
           ([1,0,1],[-1,-1,1]),([-1,1,0],[-1,-1,1]),
          ([-1,0,-1],[1,-1,-1]),([0,-1,1],[1,-1,-1]),
          ([1,1,0],[1,-1,-1]),([0,1,1],[-1,1,-1]),
          ([1,0,-1],[-1,1,-1]),([-1,-1,0],[-1,1,-1])]
    e1 = np.array([116.073,72.2954,108.774])/360
    r1 = eulerAnglesToRotationMatrix(e1)
    td = np.array([1,0,0])
    tdc = td.dot(r1)

    schmidlist = []
    for slips in slip:
        slipd = slips[0]
        slipp = slips[1]
        cosangle1 = tdc.dot(slipd) / (np.linalg.norm(tdc) * np.linalg.norm(slipd))
        cosangle2 = tdc.dot(slipp) / (np.linalg.norm(tdc) * np.linalg.norm(slipp))

        schmidfactor = cosangle1*cosangle2

        schmidlist.append(schmidfactor)

    print(schmidlist)
    plt.scatter(np.zeros((12,1)), schmidlist)"""
    plt.show()

