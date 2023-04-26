import pathlib
from PIL import Image
from tqdm import tqdm
from os import listdir
from os.path import isfile, join
import json
import shutil
import glob
from time import sleep
import cv2
import numpy as np
import argparse


def main():
    image_folder = pathlib.Path("D:/URJC/AndroidStudioImagenes")
    trash_folder = pathlib.Path("")
    report = pathlib.Path("")

    images_to_process = []

    for ext in ["*.jpg", "*.jpeg", "*.png"]:
        images_to_process.extend(image_folder.rglob(ext))

    number_of_images = len(images_to_process)

    print(number_of_images)
    with tqdm(total=number_of_images) as pbar:
        for image in images_to_process:
            with Image.open(image).convert('RGB') as img:
                if is_blurred(img)[0]:
                    print("mandar a la carpeta basura")
                else:
                    print("mandar a la carpeta de imagenes")
            sleep(0.1)
            pbar.update(1)


def is_blurred(image, threshold=90):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)
    variance = edgescv.var()
    return (variance < threshold, variance)


if __name__ == "__main__":
    main()
