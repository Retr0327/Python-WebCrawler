import urllib3
import requests
from bs4 import BeautifulSoup
urllib3.disable_warnings()
bypass={
    'from':'/bbs/Gossiping/index.html',
    'from':'/bbs/sex/index.html',
    'from':'/bbs/HatePolitics/index.html',
    'from':'/bbs/Boy-Girl/index.html',
    'yes':'yes'
}
Res=requests.session()
res=Res.post('https://www.ptt.cc/ask/over18', verify=False, data=bypass)
x=input("請輸入網址：")
print()
res=Res.get(x, verify=False,)
res.encoding='utf-8'
soup=BeautifulSoup(res.text)
print(soup.select('title')[0].text.replace(" - 批踢踢實業坊",""))
[s.extract() for s in soup('span', class_='push-ipdatetime')]           #移除特定標籤
for i, element in enumerate(soup.select(".push")):
    print(i, element.text)
