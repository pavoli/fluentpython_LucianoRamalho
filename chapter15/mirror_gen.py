# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write


if __name__ == '__main__':
    with looking_glass() as what:
        print('Alce, Kitty and Snowdrop')
        print(what)