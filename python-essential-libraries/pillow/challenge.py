from PIL import Image
import glob
import os
# make thumbmails for all images from a given directory
size = (128, 128)

images = glob.glob('*.*')

for image in images:
    if image.endswith('.jpg') or image.endswith('png') or image.endswith('jpeg'):
        fn = os.path.basename(image)
        filename, ext = os.path.splitext(fn)
        
        with Image.open(image) as img:
            img.thumbnail(size)
            img.save(filename + '.thumb' + ext)