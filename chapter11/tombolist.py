# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from random import randrange
from chapter11.tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            position = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty')
        load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))