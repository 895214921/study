from common.base import BasePage
from selenium.webdriver.common.by import By


class UserPage(BasePage):
    # def __init__(self,browser):
    #     self.browser=browser
    Balance_locat = (By.CLASS_NAME, "color_sub")
    def get_money(self):
        """获取余额"""
        el=self.browser.find_element(self.Balance_locat)
        return el.text[:-1]
