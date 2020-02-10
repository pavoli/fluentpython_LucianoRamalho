# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


coro_avg = averager()
print(next(coro_avg(10)))
print(next(coro_avg(30)))
print(next(coro_avg(5)))