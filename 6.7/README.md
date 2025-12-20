-DEFINE VISUAL FEATURES/ALGORITHM DESIGN-
Our images's theme is creatures under the sea. This program will scan over the given set of images and analyzes how many percent does the colour yellow occupied in the image, in order to determine if this image is more or less likely to have a yellow fish in it. It will print out the top 5 percentage and it's corresponding file name, listed out as a report from the 1st place to the 5th place. After that, the program will print out the file names that's likey to have a yellow fish in it. This program will also record the time it takes to do these process, and there will be a report given when the program is done running. Finally, the program will ask the user to pick a sea creature between red fish, yellow fish, or pufferfish, and it will use binary search to search for the yellow percentage of this specific image.

-FEATURE DETECTION AND EXPLANATION-
Our chosen feature will be accurately identified by using the colour(r, g, b) values, I set the values to be r > 150, g > 150, b < 100, within this range, the program can precisely identify each pixel's colour data by running through the nested loop. 



