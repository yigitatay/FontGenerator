import requests
import urllib.request
import sys, string

apiKey = "AIzaSyD1qSIU_rwgqgUh5_u-yzBUCVqEB0kA6ng"
url = "https://www.googleapis.com/webfonts/v1/webfonts?key=" + apiKey
r = requests.get(url=url)
# print(r.text)

splits = r.text.split(' ')
splits = [x.replace('\n', '')[1:-2] for x in splits if '.ttf' in x or '.otf' in splits]

fontsDir = "/Volumes/HardDrive/Fonts/downloadFonts/google/"

pageIDs = string.ascii_lowercase

for fontNo, url in enumerate(splits):
    savePath = fontsDir + str(fontNo + 1) + '.ttf'
    # urllib.request.urlretrieve(fontURL, savePath)
    if url.endswith('.tt'):
        url = url + 'f'
    r = requests.get(url)
    #print(fontNo+1,url)
    with open(savePath, 'wb') as f:
        f.write(r.content)
