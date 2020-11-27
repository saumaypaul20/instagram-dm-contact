from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd

# Change this to your own chromedriver path!
chromedriver_path = '/Users/apple/Desktop/batsy/work/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('YOUR_USERNAME')  # replace with YOUR instagram USERNAME
password = webdriver.find_element_by_name('password')
password.send_keys('YOUR_PASSWORD')  # replace with YOUR instagram PASSWORD

button_login = webdriver.find_element_by_css_selector(
    '#loginForm > div > div:nth-child(3)')
button_login.click()
sleep(3)

notnow = webdriver.find_element_by_css_selector(
    '#react-root > section > main > div > div > div > div > button')
notnow.click()
sleep(3)

notnow2 = webdriver.find_element_by_css_selector(
    'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
notnow2.click()

# replace with your TARGET USER's instagram username
target_username = 'TARGET_USERS_USERNAME'
webdriver.get('https://www.instagram.com/' + target_username)
sleep(3)

message_button = webdriver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button")
message_button.click()
sleep(5)

for x in range(1, 100):  # modify accordingly
    message_box = webdriver.find_element_by_xpath(
        "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
    message_box.send_keys('YOUR_PRANK_MESSAGE')  # replace with your message
    message_box.send_keys(Keys.ENTER)
    sleep(1)
