from PIL import ImageFont, ImageDraw, Image
import os

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrztuvwxyz"  # 52 alphanumeric

fontDir = "/Volumes/HardDrive/Fonts/allFontsClean/"  # Directory where all .ttf and .otf files are stored
dataDir = "/Volumes/HardDrive/Fonts/datasetOnlyAlpha/"  # Output dir for images

directory = os.fsencode(fontDir)
even = 0
for fontNo, file in enumerate(os.listdir(directory)):
    # For some reason, there are two of each file
    if even % 2 == 1:
        even += 1
        continue
    even += 1
    file = file.decode()
    if file[0:2] == '._':
        file = file[2:]
    if os.path.isfile(dataDir + file[:-4] + ".png"): #if that file already exists
        print("%s already exists")
        continue
    print("Font #: %d, %s" % (fontNo, file))
    searchFontSizes = True
    errorHappened = False
    i = 7  # Search across the max dimensions of each character while increasing font size until the largest dim is ~56
    while searchFontSizes:
        i += 1
        try:
            font = ImageFont.truetype(fontDir + file, i, encoding="unic")
        except:
            errorHappened = True
            break

        try:
            widths = [font.getsize(x)[0] for x in characters]
            heights = [font.getsize(x)[1] for x in characters]
        except:
            errorHappened = True
            break

        resolution = max([max(widths), max(heights)])
        if resolution == 56:
            searchFontSizes = False
        elif resolution > 56:
            i -= 1
            searchFontSizes = False

    if errorHappened:
        errorHappened = False
        continue
    canvas = Image.new('RGB', (512, 512), 'white')
    draw = ImageDraw.Draw(canvas)

    x = 0
    y = 16
    step = 0
    for char in characters:
        step += 1
        xOffset = 30 - (font.getsize(char)[0] / 2)
        draw.text((x + 4 + xOffset, y + 4), char, 'black', font)
        x += 64

        if step % 8 == 0:
            y += 64
            x = 0

    # canvas.show()
    canvas.save(dataDir + file[:-4] + ".png")
