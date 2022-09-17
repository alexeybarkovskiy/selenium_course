from selenium import webdriver
import time
import pytest

def test_registration1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element1 = browser.find_element_by_css_selector(".form-control.first:required").send_keys("Имя")
    element2 = browser.find_element_by_css_selector(".form-control.second:required").send_keys("Фамилия")
    element3 = browser.find_element_by_css_selector(".form-control.third:required").send_keys("Е-майл")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"

    time.sleep(10)
    browser.quit()

def test_registration2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    element1 = browser.find_element_by_css_selector(".form-control.first:required").send_keys("Имя")
    element2 = browser.find_element_by_css_selector(".form-control.second:required").send_keys("Фамилия")
    element3 = browser.find_element_by_css_selector(".form-control.third:required").send_keys("Е-майл")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text = browser.find_element_by_tag_name("h1").text

    assert welcome_text == "Congratulations! You have successfully registered!"

    time.sleep(10)
    browser.quit()

# Только со следующей конструкцией запустился тест:

if __name__ == "__main__":
    pytest.main()