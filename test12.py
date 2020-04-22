# -*-coding:utf-8-*-

def frange(start,stop,step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(2,20,0.5):
    print i




'''
yield，每次函数执行到yield就停止，next执行在从此处开始

'''