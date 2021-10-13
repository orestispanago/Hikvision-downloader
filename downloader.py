from selenium import webdriver
import time
import json

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 1)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", True)

profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")

browser = webdriver.Firefox(profile)
url = 'http://150.140.194.27'
browser.get(url)

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("YourUsername")
password.send_keys("YourPassword")

browser.find_element_by_xpath("//button[contains(.,'Login')]").click()
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]").click()
time.sleep(3)

browser.find_element_by_xpath('//*[@title="Capture"]').click()

time.sleep(2)

url = 'view-source:http://150.140.194.27/ISAPI/Thermal/channels/2/thermometry/1/rulesTemperatureInfo?format=json'
browser.get(url)
content = browser.find_element_by_tag_name('pre').text
parsed_json = json.loads(content)

max_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
    .get('ThermometryRulesTemperatureInfo')[0] \
    .get("maxTemperature")

min_temp = parsed_json.get('ThermometryRulesTemperatureInfoList') \
    .get('ThermometryRulesTemperatureInfo')[0] \
    .get("minTemperature")
print(min_temp, max_temp)
browser.quit()
