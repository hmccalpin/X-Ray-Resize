import os
from PIL import Image
import sys
import logging

#image_ID = os.environ['IMAGE_ID']
image_ID = "/resize-app/images/{}".format(IMAGE_ID)

im = Image.open(image_ID)
imResize = im.resize((200,200), Image.ANTIALIAS)

logging.info('resized image: {}'.format(im))

print(im)
