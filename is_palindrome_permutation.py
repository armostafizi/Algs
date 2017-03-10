#!/usr/bin/python

import re

def is_palindrome_permutation(s):
    regex = re.compile('[^a-zA-Z]')
    chars = make_dict(regex.sub('', s))
    found_odd = False
    for key, value in chars.iteritems():
        if value % 2 == 1:
            if found_odd:
                return False
            found_odd = True
    return True


def make_dict(s):
    chars = dict()
    for i in s:
        if i in chars:
            chars[i] = chars[i] + 1
        else:
            chars[i] = 1
    return chars

s = raw_input()

print(is_palindrome_permutation(s))
