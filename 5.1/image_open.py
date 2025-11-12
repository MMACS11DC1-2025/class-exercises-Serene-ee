from PIL import Image

image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()

def is_green(r, g, b):
    if 0 <= r <= 255 and 0 == g and 0 == b:
        return "green"