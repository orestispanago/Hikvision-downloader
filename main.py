from selenium import webdriver
import time

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 1)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", True)

profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/jpeg")

browser = webdriver.Firefox(profile)
url = 'http://192.168.2.10'
browser.get(url)

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys("YourUsername")
password.send_keys("YourPassword")

browser.find_element_by_xpath("//button[contains(.,'Login')]").click()
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]").click()
time.sleep(2)
browser.find_element_by_xpath('//*[@title="Capture"]').click()

time.sleep(1)
browser.quit()
