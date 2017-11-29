"""
With reference from:
http://blog.justsophie.com/image-steganography-in-python/

Program hides messages in images through LSB stenganography.

LSB = least significant bit
LSBs is useful for use in hash functions and checksums for validations purposes.
"""
from PIL import Image, ImageFont, ImageDraw
import textwrap

class LSBSteg():
    def __init__(self, im):
        self.image = im
        self.height, self.width
        self.size = self.height * self.width


def decode(file):

def encode(secret text, image):


