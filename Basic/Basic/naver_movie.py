from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

#driver = webdriver.Chrome('C:/Users/ezen/i00man_tf/Basic/Basic/chromedriver.exe')
#driver = webdriver.Chrome('C:\\Users\\ezen\\i00man_tf\\Basic\\Basic\\chromedriver.exe')
driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())


all__divs = soup.find_all('div', attrs={"class":"tit3"})
arr = [div.a.string for div in all__divs]
for i in arr:
    print(i)

driver.close()