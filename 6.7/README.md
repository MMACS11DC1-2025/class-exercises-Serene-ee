-DEFINE VISUAL FEATURES/ALGORITHM DESIGN-
Our images's theme is creatures under the sea. This program will scan over the given set of images and analyzes what percentage the colour yellow occupies in the image, in order to determine if this image is more or less likely to have a yellow fish in it. It will print out the top 5 percentages and their corresponding file names, listed out as a report from the 1st place to the 5th place. After that, the program will print out the file names that's likely to have a yellow fish in it. This program will also record the time it takes to do these process, and there will be a report given when the program is done running. Finally, the program will ask the user to pick a sea creature between red fish, yellow fish, or pufferfish, and it will use binary search to search for the yellow percentage of this specific image.

-FEATURE DETECTION AND EXPLANATION-
Our chosen feature will be accurately identified by using the colour(r, g, b) values, I set the values to be r > 150, g > 150, b < 100, within this range, the program can precisely identify each pixel's colour data by running through the nested loop. 

-TESTING AND ROBUSTNESS-
1. is_target_feature(r, g, b)
Positive test - (225, 225, 0) - Expected result: True
Negative test - (0, 0, 225) - Expected result: False

2. Selection sort
file_scores [0][0] = highest yellow percentage
file_scores [-1][0] = lowest yellow percentage

3. User interaction(error handling)
input = pUfFeRfIsH - Program should still identify the name correctly
input = 123shark - Program should print "Sorry, your input is unrecognizable." and "No result" at the end.

-PERFORMANCE ANALYSIS-
Example:
---Top 5 Highest Yellow Percentage Images (Sorted 1st place to 5th place)---
File: 6.7/yellowfish2.webp       Yellow Percentage: 32.88%
File: 6.7/yellowfish5.jpg        Yellow Percentage: 25.39%
File: 6.7/yellowfish4.jpeg       Yellow Percentage: 20.91%
File: 6.7/yellowfish3.jpg        Yellow Percentage: 18.02%
File: 6.7/yellowfish6.jpg        Yellow Percentage: 16.29%
"it took 3.191s to go through all the images and calculate percentage for each image"

The nested loop part where it's going through all the images and calculate the percentage took the most time of the program because it's complex and it handles the most job in the program. Since it's going through every single pixel in each image, and each image might have over a million pixels, so the code needs to loop over a million times for  just one image, while also needing to compare the pixel's rgb value with the criteria.

-CHALLENGES FACED-
I had one main challenge that I faced while developing the program. It was the rgb values criteria part, where I needs to build a function to compare each pixel in the given image and see if it fits the criteria. At first, I put the function in the nested loop, and it creates an error, where the output says all the images has 0 percent of yellow in it. So I tried moving the function outside the loop, and calls the function inside, so then it works well and esy to read.

-ALGORITHMIC COMPLEXITY-
1. Selection sort (O(n^2))
I used selection sort to rank the images from highest to lowest percentage. It's the most efficent way from what we've learn at this point.

2. Binary Search (O(logn))
Instead of checking every item one by one by using linear search, binary search is way more efficent because it halves the search area every step. By using binary search, it can rapidly finds the result in very few steps.
