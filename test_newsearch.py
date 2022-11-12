from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def test_newsearch():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.gosuslugi.ru/")

    # открыть РМ
    open_max = browser.find_element(By.CSS_SELECTOR, "input[class*=text]")
    open_max.click()
    # ввести запрос
    input_request = browser.find_element(By.CSS_SELECTOR, "input[class*=text]")
    input_request.send_keys("Паспорт")
    # задержка выполнения команды
    time.sleep(3)
    # отправка запроса по клавише enter
    input_request.send_keys(Keys.ENTER)
    # задержка выполнения команды
    time.sleep(3)
    # нажать на кнопку "нет нужного ответа"
    button_newsearch = browser.find_element(By.CSS_SELECTOR, ".message-button.text-plain.quiz.query")
    button_newsearch.click()
    # задержка выполнения команды
    time.sleep(3)
    # закрыть РМ
    closed_max = browser.find_element(By.CSS_SELECTOR, "button[class*=close-button")
    closed_max.click()
    # задержка выполнения команды
    time.sleep(3)
    # закрыть браузер
    browser.quit()

