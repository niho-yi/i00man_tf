
from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver.exe')
driver.implicitly_wait(3)
url = 'https://nid.naver.com/nidlogin.login'
driver.get(url)

driver.find_element_by_name('id').send_keys('')
driver.find_element_by_name('pw').send_keys('')
driver.implicitly_wait(3)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3)