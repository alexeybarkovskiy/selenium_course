import unittest
from selenium import webdriver
import time


class Test_midule1(unittest.TestCase):

    def test_1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        #заполеие обязательных полей
        input_first_name = browser.find_element_by_tag_name("input")
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input_email.send_keys("test@mail.com")
        # отпрвка заполеой формы
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected = "Congratulations! You have successfully registered!"
        self.assertEqual(expected, welcome_text, 'регистрация успеша, ура !')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.close()
        time.sleep(2)
        browser.quit()


    def test_2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        #заполеие обязательных полей
        input_first_name = browser.find_element_by_tag_name("input")
        input_first_name.send_keys("Ivan")
        input_last_name = browser.find_element_by_css_selector('input[placeholder="Input your last name"]')
        input_last_name.send_keys("Petrov")
        input_email = browser.find_element_by_css_selector("[placeholder='Input your email']")
        input_email.send_keys("test@mail.com")
         # отправка заполеой формы
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        expected = "Congratulations! You have successfully registered!"
        self.assertEqual(expected, welcome_text, 'регистрация успеша, ура !')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.close()
        time.sleep(2)
        browser.quit()

if __name__ == "__main__":
    unittest.main()
