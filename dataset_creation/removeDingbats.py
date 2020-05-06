'''
There are some fonts with only pictures, and they need to
be removed in order not to mess with the training process
'''


import os

dingbatDir = "/Volumes/HardDrive/Fonts/dingbats/"

fontsDir = "/Volumes/HardDrive/Fonts/datasetOnlyAlpha/"

i = 0
for file in os.listdir(dingbatDir):
    if os.path.isfile(fontsDir + file[:-4] + ".png"):
        os.remove(fontsDir + file[:-4] + ".png")
        print("Removed %d files" % i)
        i = i+1
