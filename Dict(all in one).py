import requests
from bs4 import BeautifulSoup

x=input(("請輸入單字："))
youdict=requests.get("https://www.youdict.com/w/"+str(x))
cha=requests.get("https://tw.ichacha.net/"+str(x)+".html")
chas=requests.get("https://tw.ichacha.net/search.aspx?q="+str(x)+"&p=2&l=en")
youdict.encoding='utf-8'
soup1=BeautifulSoup(youdict.text)
soup2=BeautifulSoup(cha.text)
soup3=BeautifulSoup(chas.text)
                 
print("詞性：")
a=soup2.find_all("ul",class_="tran_list")[0].text.replace("n.","\nn.").replace("adv.","\nadv.").replace("adj.","\nadj.").replace("vi.","\nvi.").replace("vt.","\nvt.").replace("1.","\n1.").replace("2.","\n2.").replace("3.","\n3.").replace("4.","\n4.").replace("5.","\n5.").replace("6.","\n6.").replace("7.","\n7.").replace("8.","\n8.").replace("9.","\n9.").replace("10.","\n10.").replace("11.","\n11.").replace("12.","\n12.").replace("13.","\n13.").replace("14.","\n14.").replace("15.","\n15.").replace("短語和例子","\n[短語和例子]\n")
print(a)

print()
print("中文詞源：")
for x in soup1.select("#yd-ciyuan"):
    print(soup1.select('p')[0].text)
print() 

print("例句與用法：")
print('[來源：查查辭典]')
s=soup2.select(".sent_list")
ss=soup3.select(".sent_list")
for m in s:
    n=m.find_all('li')
    o=n[0],n[1],n[2],n[3],n[4]
for p in ss:
    q=p.find_all('li')
    r=q[0],n[1],n[2],n[3],n[4]

for i, element in enumerate(o,1):
        print(str(i)+str("."), element.text.replace(".",".\n   ").replace("?","?\n   "))
for i, element in enumerate(r,6):
        print(str(i)+str("."), element.text.replace(".",".\n   ").replace("?","?\n   "))



        