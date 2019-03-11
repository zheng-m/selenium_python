#coding:utf-8
from selenium import webdriver
from module import logout,login,adduser_data,login_data
import time
from package import location
from selenium.webdriver.common.by import By


adu = adduser_data.adduser()
l_d = login_data.login_data()


driver = webdriver.Chrome()
driver.get('http://39.98.84.153:8881/login')
#driver.maximize_window()

# driver.find_element_by_id('username').clear()
# driver.find_element_by_id('username').send_keys('zhengming')
#
# driver.find_element_by_id('password').clear()
# driver.find_element_by_id('password').send_keys('zhengming')
#
# driver.find_element_by_id('login_btn').click()

login.login(driver,l_d['uname'],l_d['pwd'])

driver.switch_to.default_content()

# time.sleep(2)
dr = location
dr.findXpath(driver,'//*[@id="side-menu"]/li[3]/a').click()
# driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/a').click()
# driver.find_element_by_xpath('//*[@id="side-menu"]/li[3]/ul/li[1]/a').click()
# time.sleep(2)
# driver.switch_to.frame('iframe1')
# driver.find_element_by_id('button_post_insert').click()
#
# time.sleep(2)
# driver.find_element_by_id('login_name').send_keys(adu['addname'])
# driver.find_element_by_id('password').send_keys(adu['addpwd'])
# driver.find_element_by_id('confirmNewPassword').send_keys(adu['addpwd'])
# driver.find_element_by_id('name').send_keys(adu['addname'])
#
# driver.find_element_by_xpath('//*[@id="user_form"]/fieldset[3]/div[2]/div/div/ul').click()
# driver.find_element_by_xpath('//*[@id="user_form"]/fieldset[3]/div[2]/div/div/div/ul/li').click()
#
# checkboxs = driver.find_elements_by_css_selector('input[type=checkbox]')
# for checkbox in checkboxs:
#     checkbox.click()
#     time.sleep(1)

time.sleep(2)
#driver.quit()