import os
from PIL import Image
import sys
import logging

im = Image.open(sys.argv[2])
imResize = im.resize((200,200), Image.ANTIALIAS)

logging.info('resized image: {}'.format(im))
