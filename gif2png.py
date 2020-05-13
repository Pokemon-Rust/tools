from PIL import Image

from PIL import GifImagePlugin
import shutil
import os
import sys


if len(sys.argv) != 2:
    print('usage: python gif2png <directory>')
    sys.exit(0)

path = sys.argv[1]

print('gif2png: copying files ...')

shutil.copytree(path, path + "-g2p")

path = path + "-g2p"

for subdir, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".gif"):
            filepath = subdir + os.sep + filename
            print('gif2png: converting: ', filepath)
            pokemon = filename.split('.')[0]
            os.mkdir(subdir + os.sep + pokemon)

            try:
                img_obj = Image.open(filepath)
                for i in range(img_obj.n_frames):
                    img_obj.seek(i)
                    img_obj.save(subdir + os.sep + pokemon + os.sep + str(i) + ".png")
            except:
                print('gif2png: error occured while converting resource: ', filename)
                with open('log.txt', 'a') as handle:
                    handle.write("conv-err: " + filename + "\n")
            os.remove(filepath)