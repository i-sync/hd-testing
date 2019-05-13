"""
Page Object, Base Page
"""
import os

class Page(object):
    '''基础类，用于所有页面的继承'''
    #实例化Page类时会执行__init__方法，该方法的入参是Page类的入参
    #__init__()构造函数不能只能返回None
    def __init__(self,driver,base_url=None):
        self.driver = driver
        self.base_url = base_url
        self.timeout = 30
    #on_page()方法是URL地址的断言部分
    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)
    #单下划线_开头表示是私有的，就是通过import*时私有的方法不会被导入
    #_open()方法用于打开URL网站，并检验页面链接加载是否正确
    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        if os.environ["env"] == "live":
            assert self.on_page(),"Did not land on %s" %url
    #open()方法通过调用_open()方法打开URL网站
    def open(self):
        self._open(self.url)
    #重写定位元素的方法，loc==(By.NAME,"email"),是一个元组，Python方法中入参是元组时需要在前面加*
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
    def script(self, src):
        return self.driver.execute_script(src)