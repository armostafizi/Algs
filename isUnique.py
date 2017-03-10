#!/usr/bin/python

import sys

def is_unique(s):
    chars = dict()
    for i in s:
        if i in chars:
            return False
        chars[i]= 1
    return True


s = raw_input()

print(is_unique(s))

