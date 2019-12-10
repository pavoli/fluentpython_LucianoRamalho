# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def fidelity_promo(order):
    """
    discount 5% for customers with fidelity more than 1000
    """
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """
    discount 10% for each item in LineItem, which ordered more than 20 qty
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """
    discount 7% for order which contains not less 10 different items
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0