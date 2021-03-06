#!/usr/bin/python

import itertools

def fib():
  x,y = 0,1
  while True:
    yield x
    x,y = y, x+y

print sum(x for x in itertools.takewhile(lambda x: x <= 4000000, fib()) if x % 2 == 0)
