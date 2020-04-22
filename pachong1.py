# -
from urllib import request

url = 'http://www.baidu.com'

'''
response = RequestMethods.urlopen(GET,url)
response = request.RequestMethods().urlopen(method=GET,url=url)
response = RequestMethods().request(GET,url)
*-coding:utf-8-*-

from urllib3.request import RequestMethods
from urllib3 import request

'''
response = request.urlopen(url,timeout=10)

print(response.read.decode('utf-8'))
