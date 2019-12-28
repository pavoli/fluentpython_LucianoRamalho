# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def fibonacci(num):
    a, b = 0, 1
    while num:
        yield a
        a, b = b, a + b
        num -= 1


if __name__ == '__main__':
    f = fibonacci(10)
    for i in f:
        print(i,)