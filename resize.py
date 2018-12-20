import os
from PIL import Image
import sys
import logging

def resize(img_id):
  im = Image.open(img_id)
  imResize = im.resize((200,200), Image.ANTIALIAS)

  logging.info('resized image: {}'.format(im))

  return(im)
