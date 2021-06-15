# テロップ入れ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

def import_movie(path):
    movie = cv2.VideoCapture(path)
    return movie
