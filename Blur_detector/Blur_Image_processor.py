import pathlib
import time

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
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image_folder", required=True,
                        help="Path of the directory that contains the images to filter")
    parser.add_argument("-t", "--trash_folder", required=True,
                        help="Path of the directory that will recive the blurred images ")
    parser.add_argument("-r", "--report_folder", required=True,
                        help="Path of the .json file that will recive the report")
    args = parser.parse_args()

    image_folder = pathlib.Path(args.image_folder)
    trash_folder = pathlib.Path(args.trash_folder)
    report_folder = pathlib.Path(args.report_folder)

    extensions = ["*.jpg", "*.jpeg", "*.png"]

    images_to_process = []

    start_time = time.time()

    for ext in extensions:
        images_to_process.extend(image_folder.rglob(ext))

    number_of_images = len(images_to_process)
    number_of_blurred_images = 0
    accepted = []
    discarded = []

    with tqdm(total=number_of_images) as pbar:
        for image in images_to_process:
            with Image.open(image).convert('RGB') as img_PIL:
                blurred, score = is_blurred(img_PIL)[0], is_blurred(img_PIL)[1]
                if blurred:
                    directory_position = image.__str__().replace(image_folder.__str__(), trash_folder.__str__())
                    # Checks if the base directory already exists, if not, it creates it
                    if not os.path.exists(os.path.dirname(directory_position)):
                        os.makedirs(os.path.dirname(directory_position))
                    shutil.move(image, directory_position)
                    discarded.append({"path": str(directory_position), "score": int(score)})
                    number_of_blurred_images += 1
                else:
                    accepted.append({"path": str(image), "score": int(score)})
            sleep(0.1)
            pbar.update(1)
    end_time = time.time() - start_time

    generate_JSON_report(end_time, number_of_images, number_of_blurred_images, accepted, discarded, report_folder)


def generate_JSON_report(elapsed_time, number_of_images, blurred_images, accepted, discarded, report_folder):
    json_dict = {"elapsed_time": elapsed_time, "total_images": number_of_images, "blurred_images": blurred_images,
                 "accepted": accepted,
                 "discarded": discarded}

    report = json.dumps(json_dict)
    with open(report_folder, 'w') as rf:
        rf.write(report)


def is_blurred(image, threshold=90):
    imagecv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    graycv = cv2.cvtColor(imagecv, cv2.COLOR_BGR2GRAY)
    edgescv = cv2.Laplacian(graycv, cv2.CV_64F)
    variance = edgescv.var()
    return (variance < threshold, variance)


if __name__ == "__main__":
    main()
