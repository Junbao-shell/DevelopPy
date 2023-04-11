# 

import sys
import random
import numpy as np

def Add(a, b):
    return a + b

def MatrixAdd():
    a = np.array([[1,2,3],
                  [2,3,4],
                  [3,4,5]])
    b = np.array([[1,2,3],
                  [3,4,5],
                  [6,7,8]])
    return Add(a, b)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("input args error.")
        sys.exit()
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print("%d + %d = %d" %(a, b, Add(a, b)))
    
    print("matrix add: ")
    print(MatrixAdd())
    
