from PIL import Image

image = Image.open('landscape.jpg')
print(image.filename)
print(image.format)
print(image.size)
print(image.height)
print(image.width)
print(image.mode) # pixel format

for k,v in image.info.items():
    print(k,v)


# convert from one format to another
outfile = 'landscape.png'
image.save(outfile, 'PNG')
with Image.open(outfile) as f:
    print(f'format={f.format}')
    
    
# display image with default os image application
image.show()
