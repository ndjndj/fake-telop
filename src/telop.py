# テロップ入れ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

def dicision_path(dir, path):
    in_path = os.path.join(*[dir, path])
    out_path = os.path.join(*[dir, 'out_' + path])
    return (in_path, out_path)

def import_movie(path):
    movie = cv2.VideoCapture(path)
    return movie

def calc_movie_config(movie):
    d = {}
    d['num_of_frame'] = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    d['fps'] = movie.get(cv2.CAP_PROP_FPS)
    d['width'] = int(movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    d['height'] = int(movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
    d['fourcc'] = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    return d
