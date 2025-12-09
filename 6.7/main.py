import time
t0 = time.time()

from PIL import Image
t1 = time.time()

files = ["6.7/yellowfish1.webp", "6.7/yellowfish2.webp", "6.7/yellowfish3.jpg", "6.7/yellowfish4.jpeg", "6.7/yellowfish5.jpg", "6.7/yellowfish6.jpg", 
         "6.7/redfish1.jpg", "6.7/belugawhale.jpg", "6.7/eagleray.jpg", "6.7/killerwhale.webp", "6.7/pufferfish.webp"]

all_imgspercent = []
for imgs in files:
    file = Image.open(imgs)
    loadedFile = file.load()

    width = file.width
    height = file.height

    yellow_pixels = 0

    for x in range(width):
        for y in range(height):

            r = loadedFile[x, y][0]
            g = loadedFile[x, y][1]
            b = loadedFile[x, y][2]
            
            #yellow(function)
            if r > 150 and g > 150 and b < 100:
                yellow_pixels += 1   

    percent_yellow = 100*yellow_pixels/(width*height)

    all_imgspercent += [percent_yellow]

top5 = all_imgspercent[:5]
for item in top5:
	print("There are {:.2f} percent colour yellow in this image.".format(float(item)))
t2 = time.time()

image_open_load = t1-t0
loop = t2-t1
entire = t2-t0

timings = "It took {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(image_open_load, loop, entire)
print(timings)