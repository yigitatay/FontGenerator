from PIL import ImageFont, ImageDraw, Image
import os

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrztuvwxyz1234567890"  # alphanumeric
extra19 = "\"\'&(),.;:?!$@+-/\\~*"  # add 19 characters to round samples out to 81 characters
otherPotentialCharacters = "#^[]|{}_=%"  # other important characters you might consider adding/swaping

characters += extra19

fontDir = "/Volumes/HardDrive/Fonts/allFonts/"  # Directory where all .ttf and .otf files are stored
dataDir = "/Volumes/HardDrive/Fonts/dataset81/"  # Output dir for images

directory = os.fsencode(fontDir)
for fontNo, file in enumerate(os.listdir(directory)):
    file = file.decode()
    print("Font #: %d, %s" % (fontNo, file))
    searchFontSizes = True

    i = 7  # Search across the max dimensions of each character while increasing font size until the largest dim is ~56
    while searchFontSizes:
        i += 1
        font = ImageFont.truetype(fontDir + file, i, encoding="unic")

        widths = [font.getsize(x)[0] for x in characters]
        heights = [font.getsize(x)[1] for x in characters]

        resolution = max([max(widths), max(heights)])
        if resolution == 56:
            searchFontSizes = False
        elif resolution > 56:
            i -= 1
            searchFontSizes = False

    canvas = Image.new('RGB', (576, 576), 'white')
    draw = ImageDraw.Draw(canvas)

    x = 0
    y = 0
    step = 0
    for char in characters:
        step += 1
        xOffset = 30 - (font.getsize(char)[0] / 2)
        draw.text((x + 4 + xOffset, y + 4), char, 'black', font)
        x += 64

        if step % 9 == 0:
            y += 64
            x = 0

    # canvas.show()
    canvas.save(dataDir + file[:-4] + ".png")
