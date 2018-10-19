#import dependencies
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

# read image and convert to grayscale
image = mpimg.imread('/test_images/solidWhiteCurve.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# define a kernal size and apply Gaussian smoothing.
kernal_size = 5
blur_gray = cv2.GaussianBlur(gray, (kernal_size, kernal_size),0)

# define parameters for Canny and apply
low_threshhold = 50
high_threshold = 150
masked_edges = cv2.Canny(blur_gray, low_threshhold, high_threshold)


# define Hough transform parameters
# make a blank the same size the image to draw
rho = 1
theta = np.pi/180
threshold = 1
min_line_length = 10
max_line_gap = 1
line_image = np.copy(image)*0
#this code creates a blank to draw lines on.

# run the Hough parameters on the edge detected image
lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),min_line_length,max_line_gap)

# iterate over the output "lines" and draw lines on the blank
for line in line:
    for x1,y1,x2,y2 in lines:
        cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)
        # what does this code do?

# create a "color" binary image to combine with line line image
color_edges = np.dstack((masked_edges, masked_edges, masked_edges))

# draw lines on the edge line_image
lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0)
plt.imshow(lines_edges)
