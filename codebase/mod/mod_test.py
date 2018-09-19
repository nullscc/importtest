#!/usr/bin/env python
#-*- coding:utf8 -*-
# Power by null 2018-09-19 18:40:37

print("import mod_test....")

class Context:
    def __enter__(self):
        print("In __enter__()", id(self))
        return 'enter'

    def __exit__(self, type, value, trace):
        print("In __exit__()", id(self))

def decorate(f):
    print('excute decorate...', id(f))
    def inner():
        with Context() as context:
            print("I'm in inner", context)
            return f()
    return inner

@decorate
def test_f():
    print('excute test_f')


test_f = decorate(test_f)
