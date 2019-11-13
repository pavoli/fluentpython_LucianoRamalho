# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


import collections


Card = collections.namedtuple('Card', ['rank', 'suit'])
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JKQA')
    suit = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suit
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def choice(self):
        from random import choice

        print(choice(deck))
        print(choice(deck))
        print(choice(deck))


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]



if __name__ == '__main__':
    #card = Card('7', 'diamonds')
    #print(card)
    deck = FrenchDeck()
    #print(len(deck))
    #print(deck[0])
    #print(deck[-1])
    #deck.choice()
    #print(deck[:3])
    #print(deck[12::13])
    #just print
    #for card in deck:
    #    print(card)
    #reversed print
    #for card in reversed(deck):
    #    print(card)

    #print(Card('Q', 'hearts') in deck)
    # print(Card('Q', 'beasts') in deck)

    for card in sorted(deck, key=spades_high):
        print(card) 