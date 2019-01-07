import os
from PIL import Image
import sys
import logging

image_ID = os.environ['IMAGE_ID']

image = Image.open(image_ID)

logging.info('resized image: {}'.format(image))

new_image = image.resize((200,200), Image.ANTIALIAS)
new_image.save('/out/{}'.format(image_ID))

print(image.size) # Output: (1024, 1024)
print(new_image.size) # Output: (200, 200)

