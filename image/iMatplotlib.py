# ============================================================
# File:       iMatplotlib.py
# Author:     gaojunbao(junbaogao@foxmail.com)
# Version     0.0.1
# Date:       2023-04-12
# Brief:      使用 matplotlib 库读取图像文件
# ============================================================

import matplotlib.image as mpimg
import matplotlib.pylab as plt

def ReadImageByMatplotlib(path):
    img = mpimg.imread(path)
    print('image shape: ', img.shape, ', image data type: ', img.dtype, ', image type: ', type(img))
    
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
if __name__ == '__main__':
    ReadImageByMatplotlib('data/LenaRGB.bmp')    
    
    