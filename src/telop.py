# テロップ入れ
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

def make_video_path(dir, path):
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

def make_movie(movie, message, d):
    j = 0
    section = message[j]

    for i in range(d['num_of_frame']):
        flag, frame = movie.read()
        check = i == ext_index
        time = i / int(fps / step)

        if flag & True in check:
            if section[1] <= time <= section[2]:
                pass
        elif section[1] > time:
            pass
        else:
            if j >= len(message) - 1:
                pass
            else:
                j += 1
                section = message[j]

    return

def create_telop_movie():
    return
