# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


t = (1, 2, [30, 40])
print(t)
try:
    t[2] += [50, 60]
except:
    pass

print(t)