import os
from PIL import Image
import sys
import logging

im = Image.open(image_ID)
imResize = im.resize((200,200), Image.ANTIALIAS)

logging.info('resized image: {}'.format(im))

return(im)
