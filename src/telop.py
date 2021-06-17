# テロップ入れ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

def video_path(dir, path):
    video_path = os.path.join(*[dir, path])
    return video_path

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

def make_telop(img, message, img_width, img_height):
    font_path = 'C:\Windows\Fonts\meiryo.ttc' # need change
    font_size = 24
    font = ImageFont.truetype(font_path, font_size)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    text_w, text_h = draw.textsize(message, font)
    position = (int((img_width - text_w) / 2), int(img_height - (font_size * 1.5))) # define telop position
    draw.text(position, message, font=font, fill=(255, 255, 255, 0))
    img = np.array(img)
    return img
