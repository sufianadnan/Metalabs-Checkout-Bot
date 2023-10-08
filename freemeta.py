import time
from config import keys
import sys
from os import path 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options
driver = ('C:\\Program Files (x86)\\chromedriver.exe')
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
val = input("Enter password: ")
print(val)
url = (keys['meta_url'])
driver.get((url) + (val))
time.sleep(1.2)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(keys['email'])
driver.find_element_by_xpath('//*[@id="name"]').send_keys(keys['name'])
driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/form/div[5]/button').click()
time.sleep(2)
driver.quit()

