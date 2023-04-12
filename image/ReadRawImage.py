# ============================================================
# File:       ReadRawImage.py
# Author:     gaojunbao(junbaogao@foxmail.com)
# Version     0.0.1
# Date:       2023-04-12
# Brief:      read raw image
# ============================================================

import numpy as np
import struct as st

def Read2DArr(path, w, h, type):
    with open(path, mode='rb') as fp:
        arr = fp.read()
        img = np.frombuffer(bytearray(arr), type)
        img = img.reshape(w,h)
    return img

def Read2DUint8(path, w, h):
    return Read2DArr(path, w, h, np.uint8)

def Read2DUint16(path, w, h):
    return Read2DArr(path, w, h, np.uint16)
