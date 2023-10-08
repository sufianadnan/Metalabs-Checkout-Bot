from selenium.webdriver.common.action_chains import ActionChains
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
driver.get((keys['product_url']) + '/purchase?password=' + (val))
time.sleep(1.3)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(keys['email'])
driver.find_element_by_xpath('//*[@id="name"]').send_keys(keys['name'])
driver.find_element_by_xpath(
    '//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/form/div[3]/div').click()
time.sleep(0.1)
actions = ActionChains(driver)
actions.send_keys(keys['Card_Number'])
actions.perform()
time.sleep(0.)
actions = ActionChains(driver)
actions.send_keys(keys['Card_Month'])
actions.perform()
time.sleep(0.01)
actions = ActionChains(driver)
actions.send_keys(keys['Card_Year'])
actions.perform()
time.sleep(0.01)
actions = ActionChains(driver)
actions.send_keys(keys['CVV'])
actions.perform()
time.sleep(0.01)
actions = ActionChains(driver)
actions.send_keys(keys['Zip'])
actions.perform()
driver.find_element_by_xpath(
    '//*[@id="__next"]/div[2]/div[2]/div/div/div[2]/form/div[5]/button').click()
time.sleep(10)
