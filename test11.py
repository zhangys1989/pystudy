# -*-coding:utf-8-*-

def new_tips(args):
    def tips(func):
        def nei(c, d):
            print('start %s' %args)
            func(c, d)
            print("stop {}" .format(args))
        return nei
    return tips




@new_tips('test')
def add(a,b):
    print(a+b)






print(add(5,6))



'''
装饰器，在一些函数的执行的前后做一些公共的操作，这些操作可以在装饰器里定义

'''