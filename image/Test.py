# ============================================================
# File:       Test.py
# Author:     gaojunbao(junbaogao@foxmail.com)
# Version     0.0.1
# Date:       2023-04-12
# Brief:      test image module
# ============================================================

import cv2 as cv
import numpy as np
import ReadRawImage as rd

def TestReadUint8Type(path):
    w = 1024
    h = 1024
    arr = rd.Read2DUint16(path, w, h)
    return arr


def AdjustBC(arr):
    [w, h] = np.array(arr).shape
    arr1 = np.uint16(np.clip((cv.add(1 * arr, 30)), 0, 255 * 255))
    arr2 = np.uint16(np.clip((cv.add(1.5 * arr, 30)), 0, 255 * 255))
    arr3 = np.hstack((arr, arr1, arr2))
    return arr3

if __name__ == '__main__':
    res = TestReadUint8Type('D:/Pictures/1024.raw')
    res = AdjustBC(res)
    cv.imshow('peppers image', res)
    # print('image shape: ', res.shape)
    cv.waitKey(0)
    cv.destroyAllWindows()

