import requests
import time

def gettext(j):
    i = 0

    g= open("archive.txt","w+", encoding='utf-8')
    archive = requests.get('https://pastebin.com/archive')
    archive.text
    print(archive.text)
    g.write(archive.text)
    g.close() 

    with open ('archive.txt', 'rt') as myfile:  # Open file lorem.txt for reading text
        for line in myfile:                 # For each line, read it to a string 
            i = i + 1
            if i == 195:    
                print(line)
                break
    print(line)

    print(line[60:69])
    link = line[60:69]
    print(link)
    link = "https://pastebin.com/raw" + link 
    print(link)
    f= open("%d.txt" % (j+1),"w+", encoding='utf-8')
    j=j+1
    data = requests.get(link)
    data.text
    print(data.text)
    f.write(data.text)
    f.close()
    h= open("log.txt","w+", encoding='utf-8')
    print ( j, link, file=h )
    h.close() 
    return

x = 0
while (1):
    gettext(x)
    x=x+1
    time.sleep(7)





