# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from random import randint

def d6():
    return randint(1, 6)

d6_iter = iter(d6, 1)
print(d6_iter)

for roll in d6_iter:
    print(roll)