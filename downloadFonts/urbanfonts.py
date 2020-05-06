import requests
import urllib.request
import sys, string

fontsDir = "/Volumes/HardDrive/Fonts/downloadFonts/urbanfonts/"
searchCategory = True

pageIDs = string.ascii_lowercase

for pageID in pageIDs:

    i = 0
    searchCategory = True
    while searchCategory:

        headers = {
            "authority": "www.urbanfonts.com", "method": "GET", "path": "/fonts/fonts-a.htm", "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
             "accept-language": "en-US,en;q=0.9",
            "cookie": "__cfduid=d966aa1c87684e5a6179a1f75389dbad81586546568; __utmz=47560547.1586546574.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _fsuid=; __qca=P0-1685367457-1586546577524; PHPSESSID=sbopvaugaoq8ar0v10abrf0av5; fsbotchecked=true; __utmc=47560547; cuid=eb088b21fb3b2da758191584310034543_1589236972235; cookieconsent_status=dismiss; __utma=47560547.1313849068.1586546574.1586644969.1586656217.4; __utmt=1; __utmb=47560547.1.10.1586656217; _fssid=49b11922-853c-487f-bfb5-efd0e3c8624d; fssts=false",
            "referer": "https", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36Kit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

        i += 1
        url = "https://www.urbanfonts.com/fonts/fonts-%s_page-%d.htm" % (pageID,i)

        r = requests.get(url=url, headers=headers)
        splits = r.text.split(' ')

        splits = ["https://www.urbanfonts.com/" + x[7:-1] for x in splits if "/download?fid=" in x]
        splits = [x.replace('amp;','') for x in splits]

        if len(splits) == 0:
            searchCategory = False
            break
        else:
            print(splits, len(splits))
            for fontNo, fontURL in enumerate(splits):
                savePath = fontsDir + pageID + "_" + str(i) + "_" + str(fontNo + 1) + '.zip'
                # urllib.request.urlretrieve(fontURL, savePath)
                r = requests.get(fontURL)
                with open(savePath, 'wb') as f:
                    f.write(r.content)
