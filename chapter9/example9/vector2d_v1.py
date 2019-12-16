# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(*memv)