from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    answer_form = browser.find_element(By.ID, "answer")
    answer_form.send_keys(y)

    find_checkbox = browser.find_element(By.ID, "robotCheckbox")
    find_checkbox.click()

    find_radio = browser.find_element(By.ID, "robotsRule")
    find_radio.click()

    find_submit = browser.find_element(By.CLASS_NAME,"btn-default")
    find_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
