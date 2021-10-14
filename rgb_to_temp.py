from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import json


def get_temp_min_max(json_path):
    with open(json_path) as f:
        parsed_json = json.load(f)
    max_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
        .get('ThermometryRulesTemperatureInfo')[0] \
        .get("maxTemperature")
    min_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
        .get('ThermometryRulesTemperatureInfo')[0] \
        .get("minTemperature")
    return [min_temp, max_temp]


def get_grayscale(thermal_pic_path):
    im = Image.open(thermal_pic_path)
    rgb = np.array(im.getdata())
    return rgb[:, 0]


def rgb_to_temp(rgb_list, temp_list):
    linregress = stats.linregress(rgb_list, temp_list)
    slope = linregress.slope
    intercept = linregress.intercept
    return slope * grayscale + intercept


thermal_pic_path = "raw/20211014_140520_t.jpeg"
json_path = "raw/20211014_140520.json"

temp_min_max = get_temp_min_max(json_path)
grayscale = get_grayscale(thermal_pic_path)
rgb_min_max = [grayscale.min(), grayscale.max()]

grayscale_converted = rgb_to_temp(rgb_min_max, temp_min_max)

arr = np.reshape(grayscale_converted, [720, 1280])

plt.imshow(arr, interpolation='none')
plt.colorbar(label="Temperature °C")
plt.show()
