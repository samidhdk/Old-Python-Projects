from PIL import Image
from tqdm import tqdm
from time import sleep
import json
from tqdm import trange
import os
import shutil
import cv2
import numpy as np


def rotate():
    with Image.open("Lissandra.jpg") as img:
        img.rotate(45).show()



def bar():
    with tqdm(total=100) as pbar:
        for i in range(50):
            sleep(0.1)
            pbar.update(2)


def is_blurred(image, threshold=90):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)

    variance = edgescv.var()

    return variance < threshold, variance


#    shutil.move("blurry_images/Blurry1.jpg", "image")

def test_blur(): #JUST A TEST
    with Image.open("Lissandra.jpg") as img:
        blur = is_blurred(img)
        if blur[0]:
            print("Si esta borrosa")
        else:
            print("No está borrosa")
        print(blur)


def blur_detector(*args):
    if len(args)==2:
        args0 = args[0].split('=')
        args1 = args[1].split('=')

        source = ' '.join(map(str, args0[1:2]))
        destination = ' '.join(map(str, args1[1:2]))

        print("Source: "+source)
        print("Destination: "+destination)
        isDirectory = (os.path.isdir(source) and os.path.isdir(destination))
        if not isDirectory:
            print((os.path.isdir(source)))
            print((os.path.isdir(destination)))
            print("Error con los parametros de entrada: " + source+','+destination)
            exit();
        else:
            with tqdm(total=100) as pbar:
                for file in os.listdir(source):
                    with Image.open(source+"/"+file) as img:
                        pbar.update(100 / len(os.listdir(source)))
                        blurred = is_blurred(img)
                        if blurred[0]:
                            print("Archivo " + source + "/" + file + " movido a: " + destination)
                            sleep(0.2)

                          #  shutil.move(source+"/"+file, destination)
                        >> > import os
                        >> > filename, file_extension = os.path.splitext('/path/to/somefile.ext')
                        >> > filename
                        '/path/to/somefile'
                        >> > file_extension
                        '.ext
                          # print(source, destination)




    else:
        print("Numero incorrecto de argumentos: --image_folder='(name of your source directory)', --trash_folder='(name of you destination directory)'")


blur_detector("--image_folder=./image","--trash_folder=./blurry_images")
