# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def deco(func):
    def inner():
        print('running {}'.format(inner.__name__))
    return inner


@deco
def target():
    print('running {}'.format(target.__name__))

if __name__ == '__main__':
    target()
    print(target)