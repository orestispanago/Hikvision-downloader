import requests
from requests.auth import HTTPDigestAuth
import datetime

thermal_url = 'http://150.140.194.27/ISAPI/Streaming/channels/2/picture'
visible_url = 'http://150.140.194.27/ISAPI/Streaming/channels/1/picture'
json_url = "http://150.140.194.27/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json"


def download_img(url, fname):
    resp = requests.get(url, auth=HTTPDigestAuth('YourUsername', 'YourPassword'))
    if resp.status_code == 200:
        with open(fname, 'wb') as f:
            f.write(resp.content)
    else:
        print(resp.status_code)


date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

download_img(thermal_url, f"raw/{date_time}_t.png")
download_img(visible_url, f"raw/{date_time}_v.png")
download_img(json_url, f"raw/{date_time}.json")

# timed 0.616s from lab
# timed 1.006 from home wifi
