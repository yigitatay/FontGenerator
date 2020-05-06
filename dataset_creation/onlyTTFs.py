import os, shutil

fontDir = "/Volumes/HardDrive/Fonts/allFonts/"  # Directory where all .ttf and .otf files are stored
fontDir2 = "/Volumes/HardDrive/Fonts/allFontsClean/"

for path, subdirs, files in os.walk(fontDir):
    for name in files:

        full = os.path.join(path, name)
        if full.endswith('.ttf') or full.endswith('.otf'):
            shutil.copy(full,fontDir2+name)
            #print(full)
