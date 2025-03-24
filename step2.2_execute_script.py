from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    input_value = browser.find_element(By.ID, "answer")
    input_value.send_keys(y)

    find_checkbox = browser.find_element(By.ID, "robotCheckbox")
    find_checkbox.click()

    find_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", find_radio)
    find_radio.click()

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    time.sleep(10)
    browser.quit()