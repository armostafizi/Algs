#!/usr/bin/python

def is_permutation(s1, s2):
    chars1 = make_dict(s1)
    chars2 = make_dict(s2, chars1)
    return chars1 == chars2

def make_dict(s, prev_chars = None):
    chars = dict()
    s = s.lower()
    for i in s:
        if not i in chars:
            chars[i] = 1
        else:
            chars[i] = chars[i] + 1
        if prev_chars and i in prev_chars:
            if prev_chars[i] < chars[i]:
                print 'Uh uh!'
                return False
    return chars

s1 = raw_input()
s2 = raw_input()

print is_permutation(s1, s2)


