# -*-coding:utf-8-*-

from urllib3.request import RequestMethods
from urllib3 import request

url = 'http://www.baidu.com'

'''
response = RequestMethods.urlopen(GET,url)
response = RequestMethods().request(GET,url)

'''

response = request.RequestMethods().urlopen(method=GET,url=url)
print(response.read.decode('utf-8'))
