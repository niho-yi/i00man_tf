
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114')
soup = BeautifulSoup(url, 'lxml')

n_artist = 0
n_title=0

for i in soup.find_all(name='p', attrs=({"class":"artist"})):
    n_artist += 1
    print(str(n_artist) + " 위")
    print("아티스트:" + i.find('a').text)

print('----')

for i in soup.find_all(name='p', attrs=({"class","title"})):
    n_title += 1
    print(str(n_title) + " 위")
    print("노래제목:" + i.text)




#with open("index.html") as fp:
#    soup = BeautifulSoup(fp)
#soup = BeautifulSoup("<html>data</html>")