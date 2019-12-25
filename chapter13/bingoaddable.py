# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import itertools
from chapter11.tombola import Tombola
from chapter11.bingo import BingoCage

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = "right operand in +=  must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self

if __name__ == '__main__':
    pass