from datetime import time
from time import sleep

from selenium.webdriver.common.by import By

from common.base import BasePage


class InvestPage(BasePage):

    invest_send_locate=(By.XPATH,'//*[@class="form-control invest-unit-investinput"]')  #
    invest_btn_locate=(By.XPATH,'//*[@class="btn btn-special height_style"]')
    invest_prompt_locate=(By.CLASS_NAME,'layui-layer-btn0')
    get_success_message_locate=(By.XPATH,'(//*[@class="capital_font1 note"])[2]')
    def __init__(self,browser):
        self.browser=browser
    def fill_money(self,money):
        '''输入金额'''
        self.browser.find_element(*self.invest_send_locate).send_keys(money)
        return self
    def invest_click_invest_btn(self):
        """点击投标按钮"""
        self.browser.find_element(*self.invest_btn_locate).click()
        return self
    def get_success_pop_msg(self):
        """定位投标成功元素"""
        el=self.wait_clickable(self.get_success_message_locate)
        # self.screen_shot
        return el.text

