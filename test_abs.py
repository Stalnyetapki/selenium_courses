

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(driver):
    driver.get(link)
    driver.find_element_by_css_selector("#login_link")
