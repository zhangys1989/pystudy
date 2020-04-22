# -*-coding:utf-8-*-

import threading
import time
import random

class Mythread(threading.Thread):
    def run(self):
        print('start')
        time.sleep(2)
        print('stop')

    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name = name
        print('current thread is %s' %(self.name))


def func():
    pass




t1= Mythread('thread1')
t1.start()
t2 = threading.Thread(target=func(),name='thread2')
t2.start()
