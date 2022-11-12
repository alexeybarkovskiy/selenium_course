from selenium import webdriver
from selenium.webdriver.common.by import By

def test_lamoda():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("https://www.lamoda.ru/")
    browser.implicitly_wait(5)
    search = browser.find_element(By.CSS_SELECTOR, "input[class*=_input_xf7ng_19]")
    search.send_keys("зимняя куртка")
    button = browser.find_element(By.CSS_SELECTOR, "button[class*=x-button]")
    button.click()
    proverka = browser.find_element(By.CSS_SELECTOR, "h2[class*=_titleText_5tc8h_15]").text
    proverka_1 = "Товары по запросу «зимняя куртка»"
    assert proverka == proverka_1, f"Тест не пройден {proverka}"
    browser.quit()

