# iOpenCV.py
# date: 2023/04/11

# brief 学习基于python的OpenCV

import struct
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

print(cv.__version__)

def bytes2cv(img):
    img = np.array(bytearray(img), dtype='uint8')
    img = img.reshape(512,512,1)
    return cv.imdecode(img, cv.IMREAD_UNCHANGED)

def cv2bytes(img):
    return np.array(cv.imencode('.png', img)[1]).tobytes()

def ReadRGBImage():
    lena = cv.imread('D:/Pictures/Lena/Lena.bmp')
    cv.imshow('lena image',lena)
    print('image shape: ', lena.shape)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    print('test opencv')
    # ReadRGBImage()
    print('test opencv over')
    
