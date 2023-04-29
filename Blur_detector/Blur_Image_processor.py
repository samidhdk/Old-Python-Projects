import pathlib
from PIL import Image
from tqdm import tqdm
from os import listdir
from os.path import isfile, join
import os as os
import json
import shutil
import glob
from time import sleep
import cv2
import numpy as np
import argparse


def main():
    """
    parser = argparse.ArgumentParser
    parser.add_argument('-i', "--image_folder", required=True, help="Path of the directory that contains the images to filter")
    parser.add_argument('-t',"--trash_folder", required=True, help="Path of the directory that will recive the blurred images ")
    parser.add_argument('-r',"--report_folder", optional=True, help="Path of the directory that will recive a JSON file as a report")
    args = parser.parse_args()
    """

    image_folder = pathlib.Path("D:/URJC/AndroidStudioImagenes")
    trash_folder = pathlib.Path("C:/Users/PC/Desktop/testPython/test")
    report_folder = pathlib.Path("C:/Users/PC/Desktop/testPython")
    # image_folder = args.image_folder
    # trash_folder = args.trash_folder
    # report_folder = args.report_folder

    extensions = ["*.jpg", "*.jpeg", "*.png"]

    images_to_process = []

    for ext in extensions:
        images_to_process.extend(image_folder.rglob(ext))

    number_of_images = len(images_to_process)

    with tqdm(total=number_of_images) as pbar:
        for image in images_to_process:
            with Image.open(image).convert('RGB') as img_PIL:
                if is_blurred(img_PIL)[0]:
                    directory_position = image.__str__().replace(image_folder.__str__(), trash_folder.__str__())
                    if not os.path.exists(directory_position):
                        os.makedirs(os.path.dirname(directory_position))
                    shutil.move(image, directory_position)
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
