"""
With reference from:
http://blog.justsophie.com/image-steganography-in-python/

Program hides messages in images through LSB stenganography.

LSB = least significant bit
LSBs is useful for use in hash functions and checksums for validations purposes.


TO DO:
-PYTHON PACKAGING
-SETUP.PY (FOR USER INSTALL)
-README

"""
from PIL import Image, ImageFont, ImageDraw
import textwrap, sys, getopt, argparse

"""
Purpose: To take an image file an break the image down to its bits. Then, wrap
the desired text/hidden message within the last few bits of the image. 
"""
inputfile = ''
outputfile = ''

def write_to_text(message, image_size):
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    margin = offset = 10
    for line in textwrap.wrap(message, width = 60): #need to change?
        drawer.text((margin, offset), line, font = font)
        offset += 10
    return image_text

def decode(file):
    encode = Image.open(file)
    red_channel = encode.split()[0]

    #get the height and width coordinates
    height = encode.size[0]
    width =encode.size[1]

    decoded = Image.new("RGB", encode)
    pixels = decoded.load()

    for i in range(height):
        for j in  range(width):
            if bin(red_channel.getpixel((i,j)))[-1]== "0":
                pixels[i,j] =(255,255,255)
            else:
                pixels[i, j] = (0,0,0)
    decoded.save("images/decoded.png")

def encode(message, image):
    target  =Image.open(image)

    #rgb colors
    target_red = target.split()[0]
    target_green= target.split()[1]
    target_blue = target.split()[2]

    #get height and width
    height = target.size[0]
    width =target.size[1]

    #secret message
    target_text = write_to_text(message, target.size)
    bw_encode = target_text.convert("1")

    encode_target = Image.new("RGB", (height, width))
    pixels = encode_target.load()

    for i in range(height):
        for j in range(width):
            red_template_pix = target_red.getpixel((i,j))
            old_pix = bin(target_red.getpixel((i, j)))
            tencode_pix = bin(bw_encode.getpixel((i,j)))
            print(red_template_pix)
            red_template_pix = str(red_template_pix)
            print(red_template_pix)
            if tencode_pix[-1] =='1':
                target_red = red_template_pix[:-1] + "1"
            else:
                red_template_pix = red_template_pix[:-1] + "0"

            pixels[i, j] = (int(red_template_pix,2), target_green.getpixel((i, j)), target_blue.getpixel((i, j)))
    encode_target.save("images/encoded_image.png")

def main():
    """
    Command line function.
    Must take in a file which contains the secret message, must ask the user which image they would like the messaage
    to be wrapped in. There is no need for and output file because the program will return the same image but with the
    message wrapped in it.
    :param argv:
    :return:
    """

    parser = argparse.ArgumentParser(description="LSB Steganography Toy")

    parser.add_argument("-i","--inputfile", action= "store", dest = "inputfile", help="Stores the input image file", required= True)
    parser.add_argument("-m","--message", action= "store", dest="message",help="the string you want to encode into an image")
    parser.add_argument("-e", "--encode", action = "store_true", default = False, dest = "boolean_switch_encode", help = "set switch to true that you want to encode the image")
    parser.add_argument("-d","--decode", action = "store_true", default = False, dest = "boolean_switch_decode", help = "set switch to true that you want to decode the image")

    results = parser.parse_args()

    inputfile = results.inputfile
    message = results.message
    boolean_switch_encode = results.boolean_switch_encode
    boolean_switch_decode = results.boolean_switch_decode

    if (boolean_switch_encode == True):
        encode(message, inputfile)
        print("Encode is successful")
        print(message)

    else:
        print("Encode unsuccessful, message must be longer.")

    if (boolean_switch_decode == True):
        decode(inputfile)
        print ("Decoded file is saved in images/decoded.png")

if __name__ == '__main__':
    main()
