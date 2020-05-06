'''

This file is to remove fonts without numbers
However, this doesn't work on demos

'''

import os, shutil
import cv2, random
from PIL import ImageFont, ImageDraw, Image
import numpy as np



from fontTools.ttLib import TTFont

# def get_font_characters(font):
#     characters = {chr(y[0]) for x in font["cmap"].tables for y in x.cmap.items()}
#     return characters
#
# fontDir = "/Volumes/HardDrive/Fonts/allFontsClean/"
# removedFontsDir = "/Volumes/HardDrive/Fonts/removed_fonts/"
#
# files = os.listdir(fontDir)
#
# num_removed_fonts = 0
#
# for file in files:
#     new_file = file
#     if file[0:2] == "._":  # file names starting with ._ must be dealt with this way
#         new_file = file[2:]
#     ttf = TTFont(fontDir+new_file, 0, verbose=0, allowVID=0,
#                     ignoreDecompileErrors=True,
#                     fontNumber=-1)
#
#     char_set = get_font_characters(ttf)
#     if not(('f' in char_set) and ('F' in char_set) and ('3' in char_set)):
#         os.rename(fontDir+file, removedFontsDir+file)
#         num_removed_fonts += 1
#     ttf.close()


