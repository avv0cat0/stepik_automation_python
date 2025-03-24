from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'petstore_data.txt')  # добавляем к этому пути имя файла

    upload_file = browser.find_element(By.ID, "file")
    upload_file.send_keys(file_path)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Mike")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Dow")

    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("dow@i.ua")

    find_submit = browser.find_element(By.TAG_NAME, "button")
    find_submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
