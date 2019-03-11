#coding:utf-8
import unittest,time
from test_case import test_member,test_login
import HTMLTestRunner

testunit = unittest.TestSuite()

testunit.addTest(unittest.makeSuite(test_login.Login))
testunit.addTest(unittest.makeSuite(test_member.Member))

now = time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime())
filename = 'C:\Users\zhengming\Desktop\\test_result\\'+now+u'测试报告.html'
fp = file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'测试报告',
    description=u'用例执行情况'
)


#runner = unittest.TextTestRunner()
runner.run(testunit)