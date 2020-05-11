# Browser automation
# For webpages which may require login or javascript
# Functions to fill out forms, click submit functions
# web driver is required for selenium
from selenium import webdriver
import time

browser = webdriver.Firefox()

# browser.get('https://www.youtube.com')
browser.get('https://automatetheboringstuff.com')

element1 = browser.find_element_by_css_selector('.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a:nth-child(1)')
print(element1)
browser.execute_script("arguments[0].click();", element1)

# execute_script() synchoronously executes JavaScript in the current window/frame
# execute_script(script, *args)
# 	script: the Javascript to execute
# 	*argsL Any applicable arguments to execute

