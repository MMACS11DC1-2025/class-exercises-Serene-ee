''''
import time
t0 = time.time()

from PIL import Image
t1 = time.time()

#put the images in to a list
files = ["6.7/yellowfish1.webp", "6.7/yellowfish2.webp", "6.7/yellowfish3.jpg", "6.7/yellowfish4.jpeg", "6.7/yellowfish5.jpg", "6.7/yellowfish6.jpg", 
         "6.7/redfish1.jpg", "6.7/belugawhale.jpg", "6.7/eagleray.jpg", "6.7/killerwhale.webp", "6.7/pufferfish.webp"]

def is_target_feature(r, g, b):
    return r > 150 and g > 150 and b < 100
     
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
            
            if is_target_feature(r, g, b):
                yellow_pixels += 1 

    percent_yellow = 100*yellow_pixels/(width*height)

    all_imgspercent += [percent_yellow]
# selection sort
for i in range(len(all_imgspercent)):
     smallest = all_imgspercent[i]
     smallest_index = i

     for j in range(i+1, len(all_imgspercent)):
          if all_imgspercent[j] < smallest:
               smallest = all_imgspercent[j]
               smallest_index = j
               all_imgspercent[smallest_index], all_imgspercent[i] = all_imgspercent[i], all_imgspercent[smallest_index]

top5 = all_imgspercent[5:]
for item in top5:
	print("There are {:.2f} percent colour yellow in this image.".format(float(item)))
t2 = time.time()

image_open_load = t1-t0
loop = t2-t1
entire = t2-t0

timings = "It took {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(image_open_load, loop, entire)
print(timings)
'''
import time
t0 = time.time()

from PIL import Image
t1 = time.time()

#put the images in to a list
files = ["6.7/yellowfish1.webp", "6.7/yellowfish2.webp", "6.7/yellowfish3.jpg", "6.7/yellowfish4.jpeg", "6.7/yellowfish5.jpg", "6.7/yellowfish6.jpg", 
         "6.7/redfish1.jpg", "6.7/belugawhale.jpg", "6.7/eagleray.jpg", "6.7/killerwhale.webp", "6.7/pufferfish.webp"]

def is_target_feature(r, g, b):
    return r > 150 and g > 150 and b < 100
      
# List to store (score, filename) tuples
file_scores = []


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
                
            if is_target_feature(r, g, b):
                yellow_pixels += 1 

    percent_yellow = 100 * yellow_pixels / (width * height)

    # Store the percentage and the filename together
    file_scores.append((percent_yellow, imgs)) 

for i in range(len(file_scores)):
     smallest = file_scores[i]
     smallest_index = i

     for j in range(i+1, len(file_scores)):
          if file_scores[j] < smallest:
               smallest = file_scores[j]
               smallest_index = j
               file_scores[smallest_index], file_scores[i] = file_scores[i], file_scores[smallest_index]


# 2. Select the top 5 highest percentages (the first 5 elements of the sorted list).
top5_highest = file_scores[5:]

print("\n### Top 5 Highest Yellow Percentage Images (Sorted 5th place to 1st place) ###")
for score, filename in top5_highest:
    # Print the filename and the score
    output = "File: {}".format(filename)
    space = \t
    percentages = "Yellow Percentage: {:.2f}%".format(float(score))
    print(output,space, percentages)
t2 = time.time()

image_open_load = t1-t0
loop = t2-t1
entire = t2-t0

timings = "\nIt took {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(image_open_load, loop, entire)
print(timings)