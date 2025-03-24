from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    first_element = browser.find_element(By.ID, "num1")
    first_element_value = first_element.text

    second_element = browser.find_element(By.ID, "num2")
    second_element_value = second_element.text

    sum_value = int(first_element_value) + int(second_element_value)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_value))

    find_submit = browser.find_element(By.CLASS_NAME, "btn-default")
    find_submit.click()

finally:
    time.sleep(10)
    browser.quit()
