from PIL import Image, ImageFilter, ImageOps

infile = 'landscape.jpg'

# crop image
with Image.open(infile) as image:
    midx = image.width / 2
    midy = image.height / 2
    croparea = (midy - 400,midx - 250, midy + 400, midx + 250)
    cropimg = image.crop(croparea)
    cropimg.show()
    
# resize + rotation
with Image.open(infile) as image:
    new_img = image.resize((256, 256))
    new_img = new_img.rotate(45) # degrees
    new_img.show()
    
    
# transpose
with Image.open(infile) as image:
    new_img = image.transpose(Image.FLIP_TOP_BOTTOM)
    new_img.show()
    
# imagefilter => ex: gaussian blur
with Image.open(infile) as image:
    new_img = image.filter(ImageFilter.GaussianBlur(20))
    new_img.show()

# image processing with imageops
with Image.open(infile) as image:
    new_img = ImageOps.grayscale(image)
    new_img.show()