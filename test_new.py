import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_login(self, browser, lesson):
        link = f"{lesson}"
        browser.get(link)
        browser.implicitly_wait(5)
        textarea = browser.find_element_by_css_selector(".textarea")
        textarea.send_keys(str(math.log(int(time.time()))))
        browser.implicitly_wait(5)
        button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
        button.click()
        element_text = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
        assert element_text == "Correct!"
        browser.implicitly_wait(5)
        time.sleep(5)
        browser.quit()

if __name__ == "__main__":
    pytest.main()







