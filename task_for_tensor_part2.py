from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
images_url = 'https://yandex.ru/images/'

# Переходим на главную страницу яндекса
start_link = driver.get('https://yandex.ru/')

# Находим ссылку Картинки и переходим по ней
link_img = driver.find_element_by_css_selector('[data-id="images"]')
link_img.click()

# Проверка текущей ссылки
assert driver.current_url == images_url

# Открытие первого изображения на странице
first_page_link = driver.find_element_by_css_selector('div.cl-masonry__column:nth-child(1)>.cl-teaser:nth-child(1)>.'
                                                      'cl-teaser__wrap>a')
first_page_link.click()

# Проверяем, что открылось изображение

assert driver.current_url != images_url
try:
    driver.find_element_by_css_selector('[data-il="image__wrap"]')
except NoSuchElementException:
    print("Изображение не найдено")

# Запоминаем ссылку изображения на текущей странице
cur_img = driver.find_element_by_css_selector('[data-il="image__wrap"]')
first_img_link = cur_img.get_attribute('src')

# Нажимаем на кнопку вперед
nav_rigth = driver.find_element_by_class_name('cl-layout__nav__right')
nav_rigth.click()

# Запоминаем ссылку изображения на текущей странице
cur_img = driver.find_element_by_css_selector('[data-il="image__wrap"]')
second_img_link = cur_img.get_attribute('src')

# Проверяем, что изображения разные
assert second_img_link != first_img_link

# Нажимаем на кнопку назад, возвращаемся к первому изображению
nav_left = driver.find_element_by_class_name('cl-layout__nav__left')
nav_left.click()

# Запоминаем ссылку изображения на текущей странице
cur_img = driver.find_element_by_css_selector('[data-il="image__wrap"]')

# Проверяем, что вернулись, к тому же изображению
assert first_img_link == cur_img.get_attribute('src')















