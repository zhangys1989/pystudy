# -*-coding:utf-8-*-


import requests
from bs4 import BeautifulSoup

headers = {

    }

url='http://www.infoq.com/cn/news'
def craw2(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'lxml')
    for title_herf in soup.find_all('div',class_='new_type_block'):
        print([title.get('title')
               for title in title_herf.find_all('a') if title.get('title')])



craw2(url)




