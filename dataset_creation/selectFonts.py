'''
NOT UTILIZED FOR THIS PROJECT YET

This script can be used to go through some fonts of the dataset,
select good and bad ones manually by pressing s or d so that a
classifier can be trained to distinguish between acceptable fonts and unacceptable fonts
'''

import os, shutil
import cv2, random
from PIL import ImageFont, ImageDraw, Image
import numpy as np

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrztuvwxyz"  # 52 alpha

fontDir = "/Volumes/HardDrive/Fonts/allFontsClean/"  # Directory where all .ttf and .otf files are stored
goodDir = "/Volumes/HardDrive/Fonts/allFontsSelected/good/"
badDir = "/Volumes/HardDrive/Fonts/allFontsSelected/bad/"

directory = os.fsencode(fontDir)
files = os.listdir(directory)
random.shuffle(files)
for fontNo, file in enumerate(files):
    file = file.decode()
    print("Font #: %d, %s" % (fontNo, file))

    searchFontSizes = True
    i = 7  # Search across the max dimensions of each character while increasing font size until the largest dim is ~56
    while searchFontSizes:
        i += 1
        if file[0:2] == "._":  # file names starting with ._ must be dealt with this way
            file = file[2:]
        font = ImageFont.truetype(fontDir + file, i, encoding="unic")

        widths = [font.getsize(x)[0] for x in characters]
        heights = [font.getsize(x)[1] for x in characters]

        resolution = max([max(widths), max(heights)])
        if resolution == 56:
            searchFontSizes = False
        elif resolution > 56:
            i -= 1
            searchFontSizes = False

    canvas = Image.new('RGB', (512, 512), 'white')
    draw = ImageDraw.Draw(canvas)

    x = 0
    y = 0
    step = 0
    for char in characters:
        step += 1
        xOffset = 30 - (font.getsize(char)[0] / 2)
        draw.text((x + 4 + xOffset, y + 4), char, 'black', font)
        x += 64

        if step % 8 == 0:
            y += 64
            x = 0

    img = np.array(canvas)
    waitForKey = True
    while waitForKey:
        cv2.imshow("res", img)
        cv2.moveWindow("res", 0, 0)
        key = cv2.waitKey(0) & 0xFF
        if key == 97:
            shutil.copy(fontDir + file, goodDir + file)
            waitForKey = False
        elif key == 100:
            shutil.copy(fontDir + file, badDir + file)
            waitForKey = False
        cv2.destroyAllWindows()
