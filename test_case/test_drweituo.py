#coding:utf-8
from selenium import webdriver
from module import login,login_data,url
from selenium.webdriver.common.by import By
import unittest,time

class Drweituo(unittest.TestCase):
    u'''当日查询'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = url.get_url()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_drweituo(self):
        driver = self.driver
        driver.get(self.url)
