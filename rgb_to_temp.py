from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

min_temp = 20.9
max_temp = 23.3

fname = "150.140.194.27_02_20211014001354584.jpeg"

im = Image.open(fname)
rgb = np.array(im.getdata())
grayscale = rgb[:, 0]

min_rgb = grayscale.min()
max_rgb = grayscale.max()

linregress = stats.linregress([min_rgb, max_rgb], [min_temp, max_temp])
slope = linregress.slope
intercept = linregress.intercept

grayscale_converted = slope * grayscale + intercept

arr = np.reshape(grayscale_converted, [240, 320])

plt.imshow(arr, interpolation='none')
plt.colorbar(label="Temperature °C")
plt.show()
