from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

m, d = input('m d : ').split()
check = 0
start=time.time()
def findDocu():
    with urlopen("https://www.dimigo.hs.kr/index.php?mid=school_cafeteria") as response:
        soup = BeautifulSoup(response, 'html.parser')
        for me in soup.select('td.title > div > a'):
            comp = str(m) + "월 " + str(d) + "일 식단입니다."
            if (me.get_text() == comp):
                return me.get('href'),1
        if (check != 1): return "Too old to get!", 0

msg, check = findDocu()
if (check):
    print("Finding in " + msg + "...")
    with urlopen(msg) as response:
        soup = BeautifulSoup(response, 'html.parser')
        print(soup.select('#siDoc > ul.scFrm.top > li > div.fr > span:nth-child(3)'))
        for last in soup.select('ul>li>div.scConDoc.clearBar>div>p'):
            if (len(last.text) >= 10):
                print(last.text)
        print(time.time()-start)
        input("press any key to exit")
else:
    print(msg)