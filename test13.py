# -*-coding:utf-8-*-

a = [11,22,33]
c = a
print(id(a))
print(id(c))
print(a)
print(c)


import copy

d= copy.deepcopy(a)

print(id(d))
print(d)
a.append('55')

print(a)
print(c)
print(d)
