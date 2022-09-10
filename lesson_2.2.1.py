from selenium import webdriver
import time

link = 'http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

a = browser.find_element_by_id('num1')
b = browser.find_element_by_id('num2')
a_1 = a.text
a_2 = b.text
c = int(a_1) + int(a_2)
d = str(c)

browser.find_element_by_tag_name('select').click()
browser.find_element_by_css_selector(f"[value='{d}']").click()
button = browser.find_element_by_tag_name('button')
button.click()

time.sleep(30)
browser.quit()
