# ============================================================
# File:       iPil.py
# Author:     gaojunbao(junbaogao@foxmail.com)
# Version     0.0.1
# Date:       2023-04-12
# Brief:      使用 PIL 库读取图像文件
# ============================================================

from PIL import Image
import numpy as np
import matplotlib.pylab as plt

def ReadImageByPIL(path):
    img = Image.open(path)
    print('image size: ', img.width, 'x', img.height, ', image mode: ', img.mode, ", image format: ", img.format, ', image type: ', type(img))
    arr = np.array(img)
    arr = arr.reshape(img.width, img.height, 3)
    print('arr size: ', arr.shape)
    
    r = arr[:,:,0]
    g = arr[:,:,1]
    b = arr[:,:,2]
    gray = 0.114 * b + 0.587 * g + 0.299 * r
    gray = gray.astype(np.uint8)
    print('gray shape: ', gray.shape)

    width,height = gray.shape
    x, y = np.ogrid[0:width, 0:height]
    mask = (x - width / 2) ** 2 + (y - height / 2) ** 2 > width * height / 4
    gray[mask] = 0
    plt.figure(figsize=(10,10))
    plt.imshow(gray)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    ReadImageByPIL('data/LenaRGB.bmp')
