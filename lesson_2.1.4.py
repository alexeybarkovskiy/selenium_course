from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")
y = calc(x)
input = browser.find_element_by_tag_name("input")
input.send_keys(y)
option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
option1.click()
option2 = browser.find_element_by_css_selector("[id='robotsRule']")
option2.click()
button = browser.find_element_by_tag_name('button')
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
