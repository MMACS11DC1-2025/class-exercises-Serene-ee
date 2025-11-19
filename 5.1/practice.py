''''
from PIL import Image
import coolcolours

image_green = Image.open("kid-green.jpg").load()
image_beach = Image.open("beach.jpg").load()

image_output = Image.open("kid-green.jpg")

width = image_output.width
height = image_output.height

for i in range(width):
    for j in range(height):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        if coolcolours.is_green(r, g, b):
            beach_color = image_beach[i, j]
            image_output.putpixel((i, j), beach_color)

image_output.save("output.png", "png")


def is_light(r, g, b):
    pixel = ()
    if pixel >= 128:
        return True
    elif pixel < 128:
        return False
'''
from PIL import Image

file = Image.open("jelly_beans.jpg")
jb_image = file.load()

width = file.width
height = file.height

for x in range(width):
    for y in range(height):

        r = jb_image[x, y][0]
        g = jb_image[x, y][1]
        b = jb_image[x, y][2]
        
        if r > 150 and g > 150 and b < 100:
            output_image.putpixel((x, y), (255,255,255))
            



