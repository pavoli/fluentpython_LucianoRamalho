# -*- coding: utf-8 -*-

__author__ = 'p.olifer'
__version__ = '1.0'


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value

        return total/count
    return averager


if __name__ == '__main__':
    avg = make_averager()
    print(avg(10))
    print(avg(11))
    print(avg(12))
    print(avg(15))
    print('count ->', avg.__closure__[1].cell_contents)
    print('total ->', avg.__closure__[1].cell_contents)
    print('variables ->', [i for i in avg.__closure__])