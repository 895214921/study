from common.base import BasePage
from pages.index import IndexPage
from config.setting import HOST
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    # 为什么要用类封装，要把browser放到__init__中？
    # 共用browser参数，可以封装很多方法，不止是登陆
    #类可以继承
    url=HOST+'/Index/login.html'
    username_locat=(By.XPATH,"//*[@name='phone']")
    pwd_locat=(By.XPATH,"//*[@name='password']")
    button_locat=(By.XPATH,"//*[@class='btn btn-special']")
    get_error_msg_locat=(By.CLASS_NAME,'form-error-info')
    get_invalid_msg_locat=(By.CLASS_NAME,'layui-layer-content')

    # def __init__(self, browser):
    #     self.browser = browser

    def get(self):
        self.browser.get(self.url)
        return self

    def login_fail(self, username, pwd):
        self.browser.find_element(*self.username_locat).send_keys(username)
        self.browser.find_element(*self.pwd_locat).send_keys(pwd)
        self.browser.find_element(*self.button_locat).click()
        return self

    def login_success(self, username, pwd):
        self.browser.find_element(*self.username_locat).send_keys(username)
        self.browser.find_element(*self.pwd_locat).send_keys(pwd)
        self.browser.find_element(*self.button_locat).click()
        return IndexPage(self.browser)

    def get_error_msg(self):
        return self.browser.find_element(*self.get_error_msg_locat).text

    def get_invalid_msg(self):
        return self.browser.find_element(*self.get_invalid_msg_locat).text




