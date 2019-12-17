# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from array import array
import math

class Vector2d:
    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        classname = type(self).__name__
        return '{}({!r}, {!r})'.format(classname, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.y, self.x)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

if __name__ == '__main__':
    #print(format(Vector2d(1, 1), 'p'))
    #print(format(Vector2d(1, 1), '.3ep'))
    #print(format(Vector2d(1, 1), '.5fp'))
    v1 = Vector2d(3, 4)
    v2 = Vector2d(3.1, 4.2)
    # print(hash(v1))
    # print(hash(v2))
    # print(set([v1, v2]))
    # print(len(set([v1, v2])))
    # print(v1.__dict__)
    v1_clone = Vector2d.frombytes(bytes(v1))
    print(v1_clone)
    print(v1 == v1_clone)