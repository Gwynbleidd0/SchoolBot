from requests_html import HTMLSession
#from parsel import Selector
#from urllib.parse import urljoin
#import json
#import fille
def get_url():
    ses=HTMLSession()
    r = ses.get('https://s11028.edu35.ru/2013-06-12-15-17-31/raspisanie')
    i=0
    m=len(r.html.find('.at_icon'))
    hg = []
#date=fille.get_real_date()
#date= date +
    while i<m:
        g=1
        f=r.html.find('.at_icon')[i].attrs
        f=f.get('href')
        print(f)
        result=f.find('1 смена')
#    res=f.find(date)
        if result!=-1:
            hg.append(f)
        else:
            result=f.find('1_смена')
            if result!=-1:
                hg.append(f)
#    while g<len(f.get('href'):
#    print(result)
#    hg.append(f.get('href'))
        i=i+1
    return(hg)
#print(get_url())


#print(Selector(r.text).css('.at_icon').extract())
#Links = r.html.absolute_links
#for i in Links:
#    print(i)
