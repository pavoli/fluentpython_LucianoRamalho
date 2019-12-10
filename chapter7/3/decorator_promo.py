# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'

import chapter6.order as order_cls

promo = []

def promotion(promo_func):
    promo.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """
    discount 5% for customers with fidelity more than 1000
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item(order):
    """
    discount 10% for each item in LineItem, which ordered more than 20 qty
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order(order):
    """
    discount 7% for order which contains not less 10 different items
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


def best_promo(order):
    """
    choose max discount
    """
    return max(promo(order) for promo in promo)


def main():
    ann = order_cls.Customer('Ann Smith', 1100)
    cart = [order_cls.LineItem('banana', 4, 0.5),
            order_cls.LineItem('apple', 10, 1.5),
            order_cls.LineItem('watermellon', 5, 5.0)]
    test_order = order_cls.Order(ann, cart, best_promo)
    print(test_order)
    print(fidelity(test_order))
    print(bulk_item(test_order))
    print(large_order(test_order))


if __name__ == '__main__':
    main()