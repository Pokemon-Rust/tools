from PIL import Image

from PIL import GifImagePlugin
import os
import sys
import json


if len(sys.argv) != 2:
    print('usage: python frame_counter.py <directory>')
    sys.exit(0)

path = sys.argv[1]

dc = {}

for subdir, dirs, files in os.walk(path):
    for filename in files:
        if filename.endswith(".gif"):
            filepath = subdir + os.sep + filename
            try:
                obj = Image.open(filepath)
                print('frame_counter: frame count for file: ', filepath, ' is : ', obj.n_frames)
                dc[filepath] = obj.n_frames
            except:
                print('frame_counter: error occured while counting frames for file: ', filepath)

handle = open('frame-count.json', 'w')
handle.write(json.dumps(dc))