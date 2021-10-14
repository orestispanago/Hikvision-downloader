import os
import datetime

user = "YourUsername"
password = "YourPassword"
IP = "150.140.194.27"

base_url = f"http://{user}:{password}@{IP}"
thermal_pic_url = f"{base_url}/ISAPI/Streaming/channels/2/picture"
visible_pic_url = f"{base_url}/ISAPI/Streaming/channels/1/picture"
json_url = f"{base_url}/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json"

date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

os.system(f"wget {thermal_pic_url} -O {date_time}_t.jpeg")
os.system(f"wget {visible_pic_url} -O {date_time}_v.jpeg")
os.system(f"wget {json_url} -O {date_time}.json")

# timed 1.087s from home wifi

# os.system(f"wget -qO - {json_url}")


# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
# options = Options()
# options.headless = True
#
# browser = webdriver.Firefox(options=options)
#
# browser.get(json_url)
# content = browser.find_element_by_tag_name('pre').text
# print(content)