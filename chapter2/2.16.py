# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


fruits = ['grape', 'rapsberry', 'apple', 'banana']
print('original fruits')
print(fruits)
print(id(fruits))

sorted(fruits)
print('sorted fruits')
print(fruits)
print(id(fruits))

fruits.sort()
print('sort fruits')
print(fruits)
print(id(fruits))