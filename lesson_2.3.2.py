from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_tag_name("button")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
element_1 = browser.find_element_by_id("answer")
element_1.send_keys(y)
button_2 = browser.find_element_by_tag_name("button")
button_2.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
