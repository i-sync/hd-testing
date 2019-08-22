#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Generate fake email addresses for spam harvesters.

A pythonic Python port of Joerg Kantel's fakemail macro for Radio Userland.
It creates random e-mail addresses, optionally marked up as XHTML.

The ``prefix`` and ``postfix`` arguments were left out, since strings can
easily be prepended and appended, if needed.

For more information, see:

- http://www.schockwellenreiter.de/webworking/sonstiges/spam.html
- http://www.schockwellenreiter.de/ru/fakemail.html
- http://www.schockwellenreiter.de/images4/fakeMail.txt

:Copyright: 2006-2008 Jochen Kupperschmidt
:Date: 31-Aug-2008
:License: MIT
"""

from itertools import islice
from random import choice, randint
from string import ascii_lowercase


# top-level domains
TLDS = ('com net org mil edu de biz de ch at ru de tv com'
    'st br fr de nl dk ar jp eu it es com us ca pl').split()

def gen_name(length):
    """Generate a random name with the given number of characters."""
    return ''.join(choice(ascii_lowercase) for _ in range(length))

def address_generator():
    """Generate fake e-mail addresses."""
    while True:
        user = gen_name(randint(3, 10))
        host = gen_name(randint(4, 20))
        yield '{}@{}.{}'.format(user, host, choice(TLDS))

def pick_one_address():
    """Get one e-mail address."""
    return next(address_generator())

def markup_address(address):
    """Wrap an e-mail address in an XHTML "mailto:" anchor."""
    return '<a href="mailto:{}">{}</a>'.format((address,) * 2)

def fake_addresses(count=20, sep=', ', markup=False):
    """Generate fake e-mail addresses.

    If ``markup`` is true, turn the addresses into "mailto:" XHTML anchors.
    """
    addresses = islice(address_generator(), count)
    if markup:
        addresses = map(markup_address, addresses)
    return sep.join(addresses)

if __name__ == '__main__':
    #print(fake_addresses(sep='\n'))
    print(next(address_generator()))