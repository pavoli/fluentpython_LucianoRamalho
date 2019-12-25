# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


class A():

    def ping(self):
        print('ping:', self)


class B(A):

    def pong(self):
        print('pong:', self)


class C(A):

    def pong(self):
        print('PONG:', self)


class D(B, C):

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    d.pingpong()
    print(D.__mro__)