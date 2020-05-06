s = ""
with open('/Volumes/HardDrive/Fonts/downloadFonts/requestheadersformat.txt','w') as outFile:
    with open('/Volumes/HardDrive/Fonts/downloadFonts/requestheaders.txt', 'r') as inFile:
        for line in inFile:
            print(line)
            splits = line.split(':')
            s = s + '\"' + splits[0].replace('\n','').strip() + '\"' + ':' + '\"' + splits[1].replace('\n','').strip() + '\"' + ','
print('\n',s)


