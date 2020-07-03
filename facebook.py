from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')
searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('Youtube')

searchbutton = driver.find_element_by_xpath('//*[@id="button"]/yt-icon')
searchbutton.click()
