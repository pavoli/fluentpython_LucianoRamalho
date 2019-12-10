# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

from functools import reduce


def main(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


def main2(n):
    from operator import mul
    return reduce(mul, range(1, n+1))


if __name__ == '__main__':
    print(main(5))
    print(main2(5))
    print(callable(main(5)))
