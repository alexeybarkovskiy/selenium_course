from selenium import webdriver
import os
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
input_1 = browser.find_element_by_tag_name("input")
input_1.send_keys("Alex")
input_2 = browser.find_element_by_name("lastname")
input_2.send_keys("Petrov")
input_3 = browser.find_element_by_name("email")
input_3.send_keys("alex@mail.ru")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "file.txt")
input_4 = browser.find_element_by_name("file")
input_4.send_keys(file_path)
button = browser.find_element_by_tag_name('button')
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
