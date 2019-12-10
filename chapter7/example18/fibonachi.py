# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from chapter7.example16.clockdeco_boost import clock
import functools


@functools.lru_cache()
@clock
def fibonacci(n):
    if n<2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    print(fibonacci(6))
    print(fibonacci(30))