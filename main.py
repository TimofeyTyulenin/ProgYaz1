import requests
import sys
import time

def downFileByURL(url):
    start = time.time()
    nameFile = url.split('/')[-1] # название файла по юрл
    with open( './' + nameFile, 'wb') as g: #открытие файла на запись побайтово
        r = requests.get(url, stream=True) #гет запрос
        length = float(r.headers.get('content-length'))
        downloaded = 0
        if length is None:
            g.write(r.content)
        else:
            for chunk in r.iter_content(1024):
                downloaded += float(len(chunk))
                g.write(chunk)

                sys.stdout.write("\r %s" % downloaded + " Byte(s)")
                sys.stdout.flush()

def main():
    #url = 'https://i.pinimg.com/originals/26/2d/6c/262d6c3d5fea7af23e3ed3ae41ccfca5.jpg'
    #url = 'https://i.pinimg.com/originals/26/2d/6c/262d6c3d5fea7af23e3ed3ae41ccfca5.jpg'
    #url = 'https://img2.goodfon.ru/wallpaper/nbig/c/3c/cvety-oboi-tyulpany-tulips.jpg'
    #url = 'http://download.thinkbroadband.com/10MB.zip'
    #downFileByURL(url)
    if len(sys.argv) > 1:
        url = sys.argv[1]
        downFileByURL(url)
        print("\nFayl zagruzhen")
    else:
        print("\nssylka otsutstvuet")

if __name__ == "__main__":
    main()