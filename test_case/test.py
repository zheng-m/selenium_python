#coding:utf-8
import unittest
import random

#被测试类
class MyClass(object):
    @classmethod
    def sum(cls,a,b):
        return a + b

    @classmethod
    def div(cls,a,b):
        return a / b

    @classmethod
    def retrun(cls):
        return None

#单元测试类
class MyTest(unittest.TestCase):

    #assertEqual()方法实例
    def test_assertEqual(self):
        #断言两数之和的结果
        try:
            a,b = 1,2
            sum = 13
            self.assertEqual(a + b, sum, '断言失败,%s + %s != %s' %(a, b,sum))
        except AssertionError, e:
            print e

if __name__ == '__main__':
        unittest.main()
