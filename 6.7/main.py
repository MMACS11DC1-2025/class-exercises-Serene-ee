from PIL import Image
files = ["6.7/yellowfish1.jpg", "6.7/yellowfish2.jpg", "6.7/yellowfish3.jpg", "6.7/yellowfish4.jpg", "6.7/yellowfish5.jpg", "6.7/yellowfish6.jpg", 
         "6.7/redfish1.jpg", "6.7/belugawhale.jpg", "6.7/eagleray.jpg", "6.7/killerwhale.jpg", "6.7/pufferfish.jpg"]

for imgs in files:
    Image.open[imgs]


all_img = {"yf1_image": file.load([0])}
yf2_image = file.load([1])
yf3_image = file.load([2])
yf4_image = file.load([3])
yf5_image = file.load([4])
yf6_image = file.load([5])
rf1_image = file.load([6])
pff1_image = file.load([7])
kw_image = file.load([8])
er_image = file.load([9])
bw_image = file.load([10])

width = file.width
height = file.height

yellow_pixels = 0

for x in range(width):
    for y in range(height):

        r = all_img[yf1_image][x, y][0]
        g = all_img[x, y][1]
        b = all_img[x, y][2]
        
        #yellow
        if r > 150 and g > 150 and b < 100:
            yellow_pixels += 1   

percent_yellow = 100*yellow_pixels/(width*height)

report = "There are {:.2f} percent colour yellow in this image.".format(percent_yellow)
print(report)