from selenium import webdriver

try:
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")
except IOError:
    print('Driver not found')