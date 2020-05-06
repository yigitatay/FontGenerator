import requests
import urllib.request
import sys, string

fontsDir = "/Volumes/HardDrive/Fonts/downloadFonts/1001fonts/"
searchCategory = True

pageIDs = string.ascii_lowercase
for i in range(1000000):

    headers = {
        "authority": "www.1001freefonts.com", "method": "GET", "path": "/cfonts.php", "scheme": "https",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "__cfduid=ddc96075e52870b14065d159e55da7f051586546560; _ga=GA1.2.193837748.1586546569; _fsuid=; __gads=ID=980c68b3ef1bbd2a",
        "referer": "https", "sec-fetch-dest": "document", "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin", "sec-fetch-user": "?1", "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36"}

    i += 1
    url = "https://www.1001freefonts.com/d/%d/" % (i)
    savePath = "/Volumes/HardDrive/Fonts/downloadFonts/1001fonts/%d.zip" % i

    r = requests.get(url)
    if not r.text.strip() == "":
        with open(savePath, 'wb') as f:
            f.write(r.content)
        r = requests.get(url=url, headers=headers)

