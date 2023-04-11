# ipath.py
# date: 2023/04/10

# 学习 os, pathlib

import os 
import pathlib 

def osTest():
    print('os lib test')
    print('========== system info ==========')
    osname = os.name
    print('current system name: ', osname)
    delimeter = os.sep
    print('current system delimeter: ', delimeter)
    
    print('========== path os module interface ==========')
    currPath = os.getcwd()
    print('current absolute path: ', currPath)
    currDirFile = os.listdir()
    print('current dir has file: ', currDirFile)
    designateDir = 'd:\Work\Data\pathT'
    designateDirFile = os.listdir(designateDir)
    print('specified dir ', designateDir, ' has file: ', designateDirFile)
    # os.rename('testFile.txt', 'test001.txt')
    
    print('========== path os path submodule interface ==========')
    currFilePath = __file__
    print('current script file whole path: ', currFilePath)
    currFileAbsPath = os.path.abspath(__file__)
    print('current script file abs path: ', currFileAbsPath)
    currFileDirPath = os.path.dirname(__file__)
    print('current file dir path: ', currFileDirPath)
    
    
def pathlihbTest():
    print('path lib test')
    
if __name__ == "__main__":
    osTest()
    print()
    pathlihbTest()

