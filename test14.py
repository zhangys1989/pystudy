# -*-coding:utf-8-*-


def func(n):
    while 1 < n < 100:
        return  func(n-1)*n
    else:
        return 1



def calnum(num):
    if num != 1:
        # 递归调用自身函数
        csum = num * calnum(num - 1)
    else:
        # 设置递归出口
        csum = 1
    return csum
ret = calnum(5)
print(ret)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



print(factorial(10))

print(func(10))