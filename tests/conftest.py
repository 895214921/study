import pytest
from selenium import webdriver

from data.login_data import login_data_success
from pages.login import LoginPage


@pytest.fixture(scope='class')
def browser():
    browser=webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture()
def login(browser):  #fixture的用法，可以直接将browser当参数调用过来
    index_page=LoginPage(browser).get().login_success(login_data_success[0]['username'],login_data_success[0]['pwd'])
    return index_page