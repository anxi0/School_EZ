import requests as r
from datetime import datetime

def docuFind(month, day):
    page = 1
    while (1):
        URL='https://www.dimigo.hs.kr/index.php?mid=school_cafeteria&page='
        find=month+"월 "+day+"일 식단입니다"
        get = r.get(URL+str(page)).text
        if find in get:
            day_start = get.find(find)
            plztrim = get[day_start - 15:day_start]
            trim = plztrim[plztrim.find("=") + 1:plztrim.find("\">")]
            written = get[day_start:]
            written = written[written.find("regdate") + 7:]
            written = written[written.find('20'):written.find('20')+10]
            return trim,written
        else: page+=1

##input slicing
month, day = str(datetime.today().month),str(datetime.today().day) 

##find the document
targetnum, date = docuFind(month, day)
print("This is written : "+date)
page = "https://www.dimigo.hs.kr/index.php?mid=school_cafeteria&document_srl=" + targetnum
target_text = r.get(page).text

##morning
target_text = target_text[target_text.find("<meta name=\"description\" content=\"")+len("<meta name=\"description\" content=\""):]
target_text= target_text[:target_text.find("\" />")]
target_text = target_text.replace('&amp;amp;', '&')
target_text = target_text.replace('중식', '\n중식')
target_text = target_text.replace('석식','\n석식')
print(target_text)
input("press enter to exit :")