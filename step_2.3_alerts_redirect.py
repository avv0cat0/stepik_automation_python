from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc (x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    find_input = browser.find_element(By.ID, "answer")
    find_input.send_keys(y)

    find_submit = browser.find_element(By.TAG_NAME,"button")
    find_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
