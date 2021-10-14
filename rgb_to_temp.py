from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

min_temp = 22.9
max_temp = 20.5

fname = "picture.jpeg"

im = Image.open(fname)
rgb = np.array(im.getdata())
grayscale = rgb[:, 0]

min_rgb = grayscale.min()
max_rgb = grayscale.max()

linregress = stats.linregress([min_rgb, max_rgb], [min_temp, max_temp])
slope = linregress.slope
intercept = linregress.intercept

grayscale_converted = slope * grayscale + intercept

arr = np.reshape(grayscale_converted, [720, 1280])

plt.imshow(arr, interpolation='none')
plt.colorbar(label="Temperature °C")
plt.show()
