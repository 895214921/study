from time import sleep

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from common.base import BasePage
from pages.invest import InvestPage


class IndexPage(BasePage):
    invest_btn_locate=(By.XPATH,'(//*[@class="btn btn-special"])[1]')

    # def __init__(self,browser):
    #     self.browser=browser


    def get_user_info(self):
        """获取用户名信息"""
        locate = ('xpath', '//*[@class="mr-5"]/..')
        el=self.wait_clickable(locate,5)
        return el.text
         # return self.browser.find_element_by_class_name('mr-5').text
    def click_invest_btn(self):
        '''点击投标按钮'''
        sleep(5)
        self.wait_clickable(self.invest_btn_locate,5).click()
        return InvestPage(self.browser)
