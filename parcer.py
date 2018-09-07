from requests_html import HTMLSession
from parsel import Selector
from urllib.parse import urljoin
import json
ses=HTMLSession()
r = ses.get('https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie')
i=0
m=len(r.html.find('.at_icon'))
hg = []
while i<m:
    g=1
    f=r.html.find('.at_icon')[i].attrs
    f=f.get('href')
    print(f)
    result=f.index('1 смена',[0],[len(f)])
#    while g<len(f.get('href'):
#    print(result)
#    hg.append(f.get('href'))
    i=i+1
print(hg)


#print(Selector(r.text).css('.at_icon').extract())
#Links = r.html.absolute_links
#for i in Links:
#    print(i)
