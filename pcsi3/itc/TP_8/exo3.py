import matplotlib.pyplot as plt
import numpy as np

x1, y1 = 300, 800
x2, y2 = 1000, 1100

image = plt.imread("Gullfoss.jpg")
crop = image[y1:y2, x1:x2]

plt.imshow(crop)
# plt.axis('off')
plt.show()
