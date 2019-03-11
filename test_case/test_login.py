#coding:utf-8
from selenium import webdriver
from module import login,login_data,url
import unittest
import HTMLTestRunner
import time


class Login(unittest.TestCase):
    u'''登录'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = url.get_url()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        u'''登录'''
        driver = self.driver
        driver.get(self.url)
        l_d = login_data.login_data()
        login.login(driver,l_d['uname'],l_d['pwd'])
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
    # testunit = unittest.TestSuite()
    # testunit.addTest(Login('test_login'))
    # now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime())
    # filename = 'C:\Users\zhengming\Desktop\\test_result\\'+now+u'登录测试报告.html'
    # fp = file(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'“登录”测试报告',
    #     description=u'用例执行情况'
    # )
    # runner.run(testunit)