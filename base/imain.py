# imain.py
# date: 2023/04/10

from iTriangle import Triangle
from iShape import Shape

def TestClassInheritance():
    shape = Shape()
    shape.self_introduction()
    
    triangle = Triangle()
    triangle.self_introduction()
    print(triangle.name)

    print('is instance:')
    print(isinstance(shape, Triangle))
    print(isinstance(triangle, Shape))

if __name__ == "__main__":
    TestClassInheritance()

