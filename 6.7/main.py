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
    largest = file_scores[i]
    largest_index = i

    for j in range(i+1, len(file_scores)):
        if file_scores[j] > largest:
            largest = file_scores[j]
            largest_index = j
            file_scores[i], file_scores[largest_index] = file_scores[largest_index], file_scores[i]

# Select the top 5 highest percentages (the first 5 elements of the sorted list)
top5_highest = file_scores[:5]

print("\n---Top 5 Highest Yellow Percentage Images (Sorted 1st place to 5th place)---")
for score, filename in top5_highest:
    # Print the filename and the score
    output = "File: {}".format(filename)
    tab = '\t'
    percentages = "Yellow Percentage: {:.2f}%".format(float(score))
    print(output, tab, percentages)

print("\nAccording to the data above, these images listed below are more likely to have a yellow fish in it:")
for score, filename in file_scores:
    if score > 12:
        outputs = "{}".format(filename)
        print(outputs)

t2 = time.time()

image_open_load = t1-t0
loop = t2-t1
entire = t2-t0

timings = "\nIt took {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(image_open_load, loop, entire)
print(timings)

print("Pick a sea creature to see how many yellow percentage is in it's image.(redfish/yellowfish/pufferfish)")
fish = input().lower().strip()

if fish == "pufferfish":
    target_score = file_scores[7][0]
elif fish == "yellowfish":
    target_score = file_scores[5][0]
elif fish == "redfish":
    target_score = file_scores[6][0]
else:
    target_score = 0
    print("Sorry, your input is unrecognizable.")

def fishes(listoflist, target):
    if target_score == 0:
        return - 1
    first = 0
    last = len(listoflist)-1
    while first <= last:
        mid = int((first + last)/2)
        if listoflist[mid][0] == target:
            return listoflist[mid][0]
        elif listoflist[mid][0] > target:
            first = mid + 1
        else:
            last = mid - 1
    return - 1

print("This sea creature's image contains " + str(fishes(file_scores, target_score)) + " percent of the color yellow.")