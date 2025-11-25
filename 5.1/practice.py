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
            file.putpixel((x, y), (255,255,255))  
'''
from PIL import Image

file = Image.open("5.1/jelly_beans.jpg")
jb_image = file.load()

width = file.width
height = file.height

yellow_pixels = 0
red_pixels = 0
green_pixels = 0
blue_pixels = 0
purple_pixels = 0

for x in range(width):
    for y in range(height):

        r = jb_image[x, y][0]
        g = jb_image[x, y][1]
        b = jb_image[x, y][2]
        
        #yellow
        if r > 150 and g > 150 and b < 100:
            yellow_pixels += 1
        #red
        elif r > 175 and g < 3 and b < 3:   
            red_pixels += 1
        #green
        elif r > 30 and g > 80 and b < 30: 
            green_pixels += 1
        #blue
        elif r < 10 and g < 30 and b > 100: 
            blue_pixels += 1
        #purple
        elif r > 50 and g > 50 and b < 150:    
            purple_pixels += 1    

percent_yellow = 100*yellow_pixels/(width*height)
percent_red = 100*red_pixels/(width*height)
percent_green = 100*green_pixels/(width*height)
percent_blue = 100*blue_pixels/(width*height)
percent_purple = 100*purple_pixels/(width*height)

report = "There are {:.2f} percent yellow jellybeans.".format(percent_yellow) + "There are {:.2f} percent red jellybeans.".format(percent_red) + "There are {:.2f} percent green jellybeans.".format(percent_green) + "There are {:.2f} percent blue jellybeans.".format(percent_blue) + "There are {:.2f} percent purple jellybeans.".format(percent_purple)
print(report)

#file.save("output.png", "png")


