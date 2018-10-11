# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:37:55 2018

@author: Muhammad Abubakar
"""

from urllib.request import urlopen as up
from bs4 import BeautifulSoup as bs

link=up("amazon link")
print(link.getcode())
html=bs(link,"lxml")
product=html.title.text
print(product)

price=html.find('span',{'class','a-size-small price-info-superscript'})
print(price)
i=0
rv=html.find_all('div',{'class','a-expander-content a-expander-partial-collapse-content'})

while i <len(rv):
    print(rv[i].text)
    i+=1
    print('\n')
   