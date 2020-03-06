from selenium import webdriver

try:
    driver = webdriver.Firefox()
    driver.get("https://www.facebook.com")
except IOError:
    print('Driver not found')

    print(2*4)
    print(2899)