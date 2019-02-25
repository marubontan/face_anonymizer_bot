import argparse
import copy
from typing import Tuple

import cv2
import face_recognition
import numpy as np

from settings import REPLACED_IMAGE_PATH


def main(target_image_path):
    image = face_recognition.load_image_file(target_image_path)
    replaced_image = face_recognition.load_image_file(REPLACED_IMAGE_PATH)
    output_image = replace_faces(image, replaced_image)
    cv2.imwrite('output.jpg', cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))


def crop_image(image: np.ndarray, coordinates: Tuple[int]) -> np.ndarray:
    top, right, bottom, left = coordinates
    return image[top:bottom, left:right, :]


def resize_image(image: np.ndarray, coordinates: Tuple[int]) -> np.ndarray:
    top, right, bottom, left = coordinates
    resized_image = cv2.resize(image, dsize=(right - left, bottom - top), interpolation=cv2.INTER_CUBIC)
    return np.asarray(resized_image)


def replace_faces(image: np.ndarray, embedding_image: np.ndarray) -> np.ndarray:
    face_locations = face_recognition.face_locations(image)
    resized_embedding_images = [resize_image(embedding_image, coordinates) for coordinates in face_locations]

    output_image = copy.deepcopy(image)
    for coordinates, embedding_image in zip(face_locations, resized_embedding_images):
        top, right, bottom, left = coordinates
        output_image[top:bottom, left:right, :] = embedding_image

    return output_image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('target_image_path')
    args = parser.parse_args()
    main(args.target_image_path)
