from PIL import Image, ImageDraw, ImageFont

infile = 'landscape.jpg'

# use imagedraw routines to modify an image
# with Image.open(infile) as image:
#     draw = ImageDraw.Draw(image)
#     # draw an X on the image surface
#     draw.line((0,0) + image.size, width=40, fill=128)
#     draw.line((0, image.size[1], image.size[0], 0), width=40, fill=128)
#     image.show()


with Image.open(infile) as image:
    draw = ImageDraw.Draw(image)
    text = 'Random text'
    font = ImageFont.truetype('arial.ttf', 75)
    txt_size = draw.textsize(text, font=font) # [0->width, 1 -> height]
    location = (20, image.height - txt_size[1])
    draw.text(location, text, (255,255,255), font=font)
    image.show()