import os, zipfile

dir_name = '/Volumes/HardDrive/Fonts/downloadFonts/urbanfonts'
outdir_name = '/Volumes/HardDrive/Fonts/allFonts'
extension = ".zip"

os.chdir(dir_name) # change directory from working dir to dir with files

i = 0
for item in os.listdir(dir_name): # loop through items in dir
    if item.endswith(extension): # check for ".zip" extension
        i += 1
        print(i)
        try:
            file_name = os.path.abspath(item) # get full path of files
            zip_ref = zipfile.ZipFile(file_name) # create zipfile object
            zip_ref.extractall(outdir_name) # extract file to dir
            zip_ref.close() # close file
        except:
            pass