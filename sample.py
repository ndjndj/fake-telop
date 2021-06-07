import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import os

dir = 'movie'
path = 'Woman - 63241.mp4'
step = 1

message = [
    ['NDJ news', 1, 4],
    ['Hello, World.', 1.5, 11],
    ['this message was created by ndj.', 12, 17]
]

m_slice(path, dir, step, message)
