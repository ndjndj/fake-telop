# テロップ入れ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

def import_movie(path):
    movie = cv2.VideoCapture(path)
    return movie

def calc_movie_config(movie):
    num_of_frame = int(movie.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = movie.get(cv2.CAP_PROP_FPS)
    
    pass
