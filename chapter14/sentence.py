# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import re
import reprlib
from collections import abc

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s) ' % reprlib.repr(self.text)

if __name__ == '__main__':
    s = Sentence('"The time has come," the Warlus said,')
    print(s)
    for word in s:
        print(word)
    print(list(s))
    print(s[0])
    print(s[-1])
    print(s[4])
    print(isinstance(Sentence, abc.Iterable))