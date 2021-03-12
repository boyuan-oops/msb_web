#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep

import pytest
from selenium import webdriver


class TestDemo:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_demo(self):
        self.driver.get("https://www.meishubao.com/")
        # WebDriverWait(self.driver, 10).until()
        '''js处理页面'''

    @pytest.mark.skip
    def test_js_demo(self):
        '''
        js处理页面 滑动页面；打印一些信息；
        '''
        self.driver.get("https://fanyi.baidu.com/?aldtype=16047#en/zh/implicitly")
        self.driver.execute_script("return document.documentElement.scrollTop=100000")
        sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)")

    def test_js_demo1(self):
        '''
        js处理时间，remove readonly属性 重新赋值时间
        :return:
        '''
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a = document.getElementById('train_date'); a.removeAttribute('readonly')")
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-1'")
        sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
