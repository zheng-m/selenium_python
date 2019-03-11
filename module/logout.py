def logout(driver):
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[3]/nav/ul/li/a').click()
    driver.find_element_by_xpath('//*[@id="page-wrapper"]/div[3]/nav/ul/li/ul/li[7]/a').click()