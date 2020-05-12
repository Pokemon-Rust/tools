from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import imghdr
import os


def download_img(name, url):
    if os.path.isfile("./sprites/pokemon/" + name + ".gif"):
        print("pykachu: already downloaded resource: ", name)
        return
    flag = False
    with open("./sprites/pokemon/" + name + ".gif", 'wb') as handle:
        print("pykachu: downloading: " + name)
        response = requests.get(url, stream=True)

        if not response.ok:
            flag = True
            print("error: ", url)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
    if flag:
        try:
            os.remove("./sprites/pokemon/" + name + ".gif")
        except:
            pass


def rm_corrupt_gifs():
    for subdir, dirs, files in os.walk('./sprites/pokemon'):
        for filename in files:
            filepath = subdir + "/" + filename
            if imghdr.what(filepath) != "gif":
                print("pykachu: removing corrupt gif: ", filepath)
                os.remove(filepath)


if __name__ == '__main__':
    urls = ['https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-1-pok%C3%A9mon-r90/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-2-pok%C3%A9mon-r91/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-3-pok%C3%A9mon-r92/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-4-pok%C3%A9mon-r93/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-5-pok%C3%A9mon-r94/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-6-pok%C3%A9mon-r95/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-7-pok%C3%A9mon-r96/',
            'https://projectpokemon.org/docs/spriteindex_148/3d-models-generation-8-pok%C3%A9mon-r123/']

    rm_corrupt_gifs()

    for url in urls:
        print('pykachu: scraping url: ', url)
        resp = urlopen(url)
        soup = BeautifulSoup(resp, 'html.parser')
        for image in soup.findAll('img'):
            image_src = image.get('src')
            subdir = image_src.split('/')[-2]
            pokemon = image_src.split('/')[-1].split('.')[0]

            if not os.path.isdir('./sprites/pokemon/' + subdir):
                os.mkdir('./sprites/pokemon/' + subdir)
            try:
                download_img(subdir + '/' + pokemon, image_src)
            except:
                pass
