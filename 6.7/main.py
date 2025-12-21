import time
# Start the initial timer for calculating the time each part of the program takes
t0 = time.time()

from PIL import Image
# Track the time the program takes to load the images
t1 = time.time()

# Put the images in to a list
files = ["6.7/yellowfish1.webp", "6.7/yellowfish2.webp", "6.7/yellowfish3.jpg", "6.7/yellowfish4.jpeg", "6.7/yellowfish5.jpg", "6.7/yellowfish6.jpg", 
         "6.7/redfish1.jpg", "6.7/belugawhale.jpg", "6.7/eagleray.jpg", "6.7/killerwhale.webp", "6.7/pufferfish.webp"]

# Determine if the pixel is yellow
def is_target_feature(r, g, b):
    return r > 150 and g > 150 and b < 100
      
# A list to store (score, filename) tuples
file_scores = []

for imgs in files:
    # Open the images in the list(files)
    file = Image.open(imgs)
    loadedFile = file.load()

    width = file.width
    height = file.height

    # Initialize the number for the yellow pixels
    yellow_pixels = 0

    # Nested loop - go through every single pixel of the image
    for x in range(width):
        for y in range(height):

            r = loadedFile[x, y][0]
            g = loadedFile[x, y][1]
            b = loadedFile[x, y][2]

            # If pixel matches the yellow criteria, yellow_pixels +1    
            if is_target_feature(r, g, b):
                yellow_pixels += 1 

    # Calculates the percentage of yellow pixels in the image
    percent_yellow = 100 * yellow_pixels / (width * height)

    # Store the percentage and the filename together
    file_scores.append((percent_yellow, imgs)) 
t2 = time.time()

# Selection sort - sort the files and percentage from highest to lowest percent of yellow images
for i in range(len(file_scores)):
    # Fisrt element is the biggest until it found something bigger
    largest = file_scores[i]
    largest_index = i

    for j in range(i+1, len(file_scores)):
        # If found a bigger one
        if file_scores[j] > largest: 
            largest = file_scores[j]
            largest_index = j

            # Swap with the first element
            file_scores[i], file_scores[largest_index] = file_scores[largest_index], file_scores[i]
t3 = time.time()

# Select the top 5 highest percentages (the first 5 elements of the sorted list)
top5_highest = file_scores[:5]

# Display the percentages and the corresponding file name out
print("\n---Top 5 Highest Yellow Percentage Images (Sorted 1st place to 5th place)---")
for score, filename in top5_highest:
    # Print the filename and the score
    output = "File: {}".format(filename)
    tab = '\t'
    percentages = "Yellow Percentage: {:.2f}%".format(float(score))
    print(output, tab, percentages)

# Display the file name that's likely has a yellow fish in it out
print("\nAccording to the data above, these images listed below are more likely to have a yellow fish in it:")
for score, filename in file_scores:
    if score > 12:
        outputs = "{}".format(filename)
        print(outputs)

# Track the time it takes to do all of these
t3 = time.time()

# Calculate the time it takes for each part
image_open_load = t1-t0
loop = t2-t1
entire = t3-t0

# Display the times out
timings = "\nIt took {:.3f}s to load the image, {:.3f}s to go through all the image and calculate percentage for each image. All in all it took {:.3f}s.".format(image_open_load, loop, entire)
print(timings)

# User interaction - ask user to pick a sea creature
print("Pick a sea creature to see how many yellow percentage is in it's image.(redfish/yellowfish/pufferfish)")
fish = input().lower().strip()

# Connect the user's input to their percentage
if fish == "pufferfish":
    target_score = file_scores[7][0]
elif fish == "yellowfish":
    target_score = file_scores[5][0]
elif fish == "redfish":
    target_score = file_scores[6][0]
else:
    # Handles potential errors
    target_score = 0
    print("Sorry, your input is unrecognizable.")

# Binary search - finds the percentage's corresponding file name in the sorted list
def fishes(listoflist, target):
    # Handles potential errors if the user has invalid input
    if target_score == 0:
        return
    first = 0
    last = len(listoflist)-1
    while first <= last:
        # Find the middle index
        mid = int((first + last)/2)
        # If found the target
        if listoflist[mid][0] == target:
            return listoflist[mid][0]
        # If middle is larger than target
        elif listoflist[mid][0] > target:
            first = mid + 1
        # If middle is smaller than target
        else:
            last = mid - 1
    return - 1

# Display the file name of what's the user is asking for by using binary search
if target_score == 0:
    # Handles potential errors
    print("No result")
else:
    print("This sea creature's image contains " + str(fishes(file_scores, target_score)) + " percent of the color yellow.")