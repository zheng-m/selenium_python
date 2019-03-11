#coding:utf-8
from selenium import webdriver
from module import login,login_data,adduser_data,url
from package import location
import unittest
import HTMLTestRunner
import time


class Member(unittest.TestCase):
    u'''会员管理'''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = url.get_url()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_adduser(self):
        u'''新增会员'''
        driver = self.driver
        driver.get(self.url)
        l_d = login_data.login_data()
        login.login(driver, l_d['uname'], l_d['pwd'])
        a_d = adduser_data.adduser()
        time.sleep(3)
        #调用location.py文件的定位方法
        dr = location
        #进入用户管理
        dr.findXpath(driver,'//*[@id="side-menu"]/li[3]/a').click()
        dr.findXpath(driver,'//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()
        time.sleep(2)
        #进入新增页面
        driver.switch_to.frame('iframe1')
        dr.findId(driver,'button_post_insert').click()
        time.sleep(2)
        #定位用户名
        dr.findId(driver,'login_name').send_keys(a_d['addname'])
        #定位密码
        dr.findId(driver,'password').send_keys(a_d['addpwd'])
        #定位确认密码
        dr.findId(driver,'confirmNewPassword').send_keys(a_d['addpwd'])
        #定位姓名
        dr.findId(driver,'name').send_keys(a_d['addname'])
        #系统权限
        dr.findXpath(driver,'//*[@id="user_form"]/fieldset[3]/div[2]/div/div/ul').click()
        dr.findXpath(driver,'//*[@id="user_form"]/fieldset[3]/div[2]/div/div/div/ul/li').click()
        #定位用户角色复选框
        checkboxs = dr.findsCss(driver,'input[type=checkbox]')
        for checkbox in checkboxs:
            checkbox.click()
            time.sleep(1)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
    # testunit = unittest.TestSuite()
    # testunit.addTest(Member('test_adduser'))
    # now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime())
    # filename = 'C:\Users\zhengming\Desktop\\test_result\\'+now+u'会员管理测试报告.html'
    # fp = file(filename,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'“会员管理”测试报告',
    #     description=u'用例执行情况'
    # )
    # runner.run(testunit)