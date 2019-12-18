# -*- coding: utf-8 -*-
__author__ = 'p.olifer'

import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JKQA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value):
        self._cards[position] = value

    def __delitem__(self, position):
        del self._cards[position]

    def insert(self, position, value):
        self._cards.insert(position, value)


if __name__ == '__main__':
    pass