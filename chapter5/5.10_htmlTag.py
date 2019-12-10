# -*- coding: utf-8 -*-
__author__ = 'p.olifer'


def factorial(n):
    """
    :param n: int
    :return: n!
    """
    return 1 if n < 2 else n * factorial(n-1)


def tag(name, *content, cls=None, **attrs):
    """
    generate one or several html-tags
    :param name: tag name
    :param content: tag content
    :param cls: css class
    :param attrs: taf attributes
    :return: html-tag
    """

    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


def test(text, max_len=80):
    pass


if __name__ == '__main__':
    # print(factorial.__name__)
    # print(factorial.__annotations__)
    # print(factorial.__class__)
    # print(factorial.__code__)
    # print(factorial.__defaults__)
    # print(factorial.__dict__)
    # print(factorial.__dir__())
    # print(factorial.__doc__)
    # print(all([]))
    # print(any([]))
    # print(any(set('133')))
    # print(any(['133']))
    # print(tag('br'))
    # print(tag('p', 'hello'))
    # print(tag('p', 'hello', 'world'))
    # print(tag('p', 'hello', id=33))
    # print(tag('p', 'hello', 'world', cls='sidebar'))
    """
    tag_name = {'name': 'img',
                'title': 'Sunset Boulevard',
                'src': 'sunset.jpg',
                'cls': 'framed'
                }
    """
    # print(tag(id=33, source='sunset.jpeg', title='Sunset Boulevard', cls='sidebar', name='p'))
    print(test.__defaults__)
    print(test.__code__.co_varnames)
