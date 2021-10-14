import requests
from requests.auth import HTTPDigestAuth

thermal_url = 'http://150.140.194.27/ISAPI/Streaming/channels/2/picture'
visible_url = 'http://150.140.194.27/ISAPI/Streaming/channels/1/picture'
json_url = "http://150.140.194.27/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json"


def download_img(url, fname):
    resp = requests.get(url, auth=HTTPDigestAuth('YourUsername', 'YourPassword'))
    with open(fname, 'wb') as f:
        f.write(resp.content)


download_img(thermal_url, "raw/thermal.png")
download_img(visible_url, "raw/visible.png")
download_img(json_url, "raw/temps.json")

# timed 0.616s from lab
