#Reference: https://github.com/saprative/AudioSteganography/blob/master/main.py

import os, sys, stegLSB, bit

def main(file):
    #get inputfile
    inputFile = file
    isFile = False
    if os.path.isfile(inputFile):
        isFile = True
    else:
        return IOError("File does not exist")
