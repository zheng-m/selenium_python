#coding:utf-8
def login(driver,username,password):
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(username)

    driver.find_element_by_id('password').clear()
    driver.find_element_by_id('password').send_keys(password)

    driver.find_element_by_id('login_btn').click()

    driver.switch_to.frame('iframe0')
    t1 = driver.find_element_by_css_selector('body > div > div > strong').text
    if t1 == u'郑明':
        print t1 + ' ' + u'登录成功！'
    else:
        print u'登录失败！！！'
        driver.get_screenshot_as_file('C:\Users\zhengming\Desktop\\'+u"登录失败.png")
    driver.switch_to.default_content()