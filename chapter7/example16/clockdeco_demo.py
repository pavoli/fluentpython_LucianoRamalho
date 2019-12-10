# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import time
# from chapter7.example16.clockdeco import clock
from chapter7.example16.clockdeco_boost import clock

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! = ', factorial(6))