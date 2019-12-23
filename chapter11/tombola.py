# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import  abc

class Tombola(abc.ABC):

    @abc.abstractmethod
    def load(self, iterable):
        """add elements from itarebla object"""

    @abc.abstractmethod
    def pick(self):
        """
        function return a random element
        this method should raise an exception 'LookupError'
        if object is empty
        """

    def loaded(self):
        """
        return 'True' if exists only 1 element, else return 'False'
        """
        return bool(self.inspect())

    def inspect(self):
        """
        return sorted tuple
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))

class Fake(Tombola):
    def pick(self):
        return 13


if __name__ == '__main__':
    f = Fake()