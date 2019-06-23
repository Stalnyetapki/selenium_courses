import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def calc():
    return str(math.log(int(time.time())))


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('w3c', False)
    driver = webdriver.Chrome(chrome_options=opt)
    yield driver
    print("\nquit browser..")
    driver.quit()


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1', 'https://stepik.org/lesson/236896/step/1',
                                  'https://stepik.org/lesson/236897/step/1', 'https://stepik.org/lesson/236898/step/1',
                                  'https://stepik.org/lesson/236899/step/1', 'https://stepik.org/lesson/236903/step/1',
                                  'https://stepik.org/lesson/236904/step/1', 'https://stepik.org/lesson/236905/step/1'])
class TestPagesOfStepik():
    def test_guest_should_see_login_link(self, driver, link, calc):
        driver.get(link)
        # Ищем строку и вводим ответ из фикстуры calc
        input_answer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'textarea')))
        input_answer.send_keys(calc)
        # Ждем, пока появится кнопка отправки и нажимаем на нее
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'submit-submission ')))
        button.click()
        # Проверяем, что ответ правильный
        answer = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        value = answer.text
        assert value == 'Correct!', 'Answer not correct'
