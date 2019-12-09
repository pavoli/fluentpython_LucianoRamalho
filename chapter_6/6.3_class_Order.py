# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

from collections import namedtuple
import chapter_6.promotions as promo_module
import inspect

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order: # Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


# promos = [fidelity_promo, bulk_item_promo, large_order_promo]
"""
promos = [globals()[name] for name in globals()
          if name.endswith('_promo')
          and name != 'best_promo']
          """

promos = [func for name, func in inspect.getmembers(promo_module, inspect.isfunction)]

def best_promo(order):
    """
    choose max discount
    """
    return max(promo(order) for promo in promos)

if __name__ == '__main__':
    joe = Customer('John Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]
    banana_cart = [LineItem('banana', 30, 0.5),
                   LineItem('apple', 10, 1.5)]
    long_order = [LineItem(str(item_code), 1, 1.0)
                  for item_code in range(10)]
    # print(Order(joe, cart, fidelity_promo))
    # print(Order(ann, cart, fidelity_promo))
    # print(Order(joe, long_order, bulk_item_promo))
    # print(Order(joe, cart, large_order_promo))
    # print(Order(joe, long_order, best_promo))
    # print(Order(joe, banana_cart, best_promo))
    print(Order(ann, cart, best_promo))