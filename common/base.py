import logging
import os
import datetime
import time

import pyautogui
import pyperclip
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

from config import setting

DEFAULT_TIMEOUT=10
DEFAULT_POLL=0.5
class BasePage():
    host=''
    def __init__(self,browser):
        self.browser=browser

    def wait_clickable(self, locate,timeout=10):
        """显性等待，等待元素被点击"""
        try:
            el = WebDriverWait(self.browser, timeout=timeout).until(expected_conditions.element_to_be_clickable(locate))
        except Exception as e:
                self.screen_shot()
                logging.error(f'定位元素失败{e}')
        return el

    def wait_visibility_of_element_located (self,timeout,locate):
        """显性等待，元素是否可见"""
        el=WebDriverWait(self.browser,timeout=timeout).until(expected_conditions.visibility_of_element_located(locate))
        return el
    def wait_presence_of_element_located(self,timeout,locate):
        """显性等待，元素是否出现"""
        el = WebDriverWait(self.browser, timeout=timeout).until(expected_conditions.presence_of_element_located(locate))
        return el

    def screen_shot(self):
        """获取截图"""
        # times= time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pic_name=os.path.join(setting.IMG_PATH,str(int(time.time()))+ '.png')
        self.browser.save_screenshot(pic_name)

    def refresh(self):
        """刷新"""
        self.brower.refresh()
        return self

    def goto(self,url:str):
        """访问url"""
        if url.startswith(('http://','https://')):
            return self.browser.get(url)
        if not url.startswith("/"):
            return ValueError('url must start with slash/.')
        url=self.host+url
        return self.browser.get(url)

    def click(self,locator):
        """点击"""
        el=self.wait_clickable(locator)
        el.click()
        return self

    def wait_element(self,locator,timeout=DEFAULT_TIMEOUT,poll=DEFAULT_POLL):
        """智能等待"""
        used_time=0
        while used_time < timeout:
            try:
                time.sleep(poll)
                return self.browser.find_element(locator)
            except Exception as e:
                used_time=used_time+poll
            raise Exception(f'找不到元素{locator}')

    def sendkeys(self,locator,words):
        """输入"""
        el=self.wait_element(locator)
        el.send_keys(words)
        return self

    def double_click(self,locator):
        '''双击'''
        el=self.wait_element(locator)
        ac=ActionChains(self.browser)
        ac.double_click(el).perform()
        return el

    def right_click(self,locator):
        '''右击'''
        el=self.wait_element(locator)
        ac=ActionChains(self.browser)
        ac.context_click(el).perform()
        return self

    def drag_and_drop(self,start,over):
        '''拖拽'''
        el=self.wait_element(start)
        el2=self.wait_element(over)
        ac=ActionChains(self.browser)
        ac.drag_and_drop(el,el2).perform()
        return self

    def scroll_To(self,width,height):
        '''拖动页面窗口'''
        self.browser.execute_script('window.scrollTo({}{})'.format(width,height))
        return self

    def scroll_to_bottom(self):
        '''拖动页面到最底部'''
        self.browser.execute_script('window.scrillTo(0,document.body.scrollHeight)')
        return self

    def upload(self,locator,file):
        '''上传文件'''
        el=self.wait_element(locator)
        if el.tag_name=='input':
            el.send_keys(file)
            return self
        el.click()
        pyperclip.copy(file)
        time.sleep(.2)
        pyautogui.hotkey('ctrl','v')
        pyautogui.press('enter',presses=2)
        return self

    def set_attr(self,locator,prop_name,prop_valu):
        """修改页面属性"""
        el=self.wait_element(locator)
        jscode='arguments[0].{}="{}"'.format(prop_name,prop_valu)
        self.browser.execute_script(jscode,el)