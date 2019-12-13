# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)
print('t1_id={}', id(t1[-1]))
print('t2_id={}', id(t2[-1]))

t1[-1].append(99)
print('t1=', t1)
print('t1_id={}', id(t1[-1]))
print(t1 == t2)