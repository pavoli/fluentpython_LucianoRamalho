# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s) ' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))


if __name__ == '__main__':
    print(all([]))
    print(all({}))
    print(all(set()))
    print(any([]))
    print(any({}))
    print(any(set('1')))