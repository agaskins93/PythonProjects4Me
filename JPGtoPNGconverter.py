# JPGtoPNGConverter.py Pokedex/ new/

import sys
import os
from PIL import Image

#first and second argument
#check if new equiset and not create
#loop throuhg pokedx
#conver image sto pngsave to new folerd

def convert(folder1, folder2):
    print(folder1)

    if not os.path.exists(folder2):
        os.makedirs(folder2)

    os.listdir(folder1)
    for filename in os.listdir(folder1):

        img = Image.open(f'./ImageProcessor/Pokedex/{filename}')
        filename = filename.removesuffix('.jpg')
        print(filename)
        img.save(f'./pngConvert/{filename}.png','png')


convert(sys.argv[1],sys.argv[2])
