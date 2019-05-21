"""
Page Object, Base Page
"""
import os
import logging
from contextlib import contextmanager
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.action_chains import ActionChains

class Page(object):
    '''基础类，用于所有页面的继承'''
    #实例化Page类时会执行__init__方法，该方法的入参是Page类的入参
    #__init__()构造函数不能只能返回None
    def __init__(self,driver,base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
        self.logger = logging.getLogger(__name__)
    #on_page()方法是URL地址的断言部分
    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)
    #单下划线_开头表示是私有的，就是通过import*时私有的方法不会被导入
    #_open()方法用于打开URL网站，并检验页面链接加载是否正确
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        if "env" in os.environ and os.environ["env"] == "live":
            assert self.on_page(),"Did not land on %s" %url
    #open()方法通过调用_open()方法打开URL网站
    def open(self):
        self._open(self.url)
    #重写定位元素的方法，loc==(By.NAME,"email"),是一个元组，Python方法中入参是元组时需要在前面加*
    def find_element(self,loc):
        return self.driver.find_element(*loc)
    def find_elements(self,loc):
        return self.driver.find_elements(*loc)
    def script(self, src):
        return self.driver.execute_script(src)

    #click element
    def click_element(self, loc, refresh_page=False, timeout=30):
        if refresh_page:
            with self.wait_for_page_load(timeout):
                self.find_element(loc).click()
        else:
            self.find_element(loc).click()

    #select element
    def select_element_by_value(self, loc, value, refresh_page=False, timeoue=30):
        if refresh_page:
            with self.wait_for_page_load(timeoue):
                Select(self.find_element(loc)).select_by_value(value)
        else:
            Select(self.find_element(loc)).select_by_value(value)
    #select element
    def select_element_by_index(self, loc, index, refresh_page=False, timeoue=30):
        if refresh_page:
            with self.wait_for_page_load(timeoue):
                Select(self.find_element(loc)).select_by_index(index)
        else:
            Select(self.find_element(loc)).select_by_index(index)
    #select element
    def select_element_by_visible_text(self, loc, text, refresh_page=False, timeoue=30):
        if refresh_page:
            with self.wait_for_page_load(timeoue):
                Select(self.find_element(loc)).select_by_visible_text(text)
        else:
            Select(self.find_element(loc)).select_by_visible_text(text)

    #textbox input value
    def input_element_value(self, loc, value):
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(value)

    # mouseover element
    def mouseover_element(self,loc):
        action = ActionChains(self.driver)
        element = self.find_element(loc)
        action.move_to_element(element).perform()
        return element
    #key_down
    def key_Action(self,keyValue):
        action=ActionChains(self.driver)
        action.key_down(keyValue)
        action.key_up(keyValue)
        action.perform()
    @contextmanager
    def wait_for_page_load(self, timeout=30):
        """
        wait for page load
        URL: https://blog.codeship.com/get-selenium-to-wait-for-page-load/
        :param timeout:
        :return:
        """
        old_page = self.driver.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.driver, timeout).until(
            staleness_of(old_page)
        )
    #wait page element
    def wait_for_page_element(self,timeout,loc):
        WebDriverWait(self.driver,timeout).until(loc)
