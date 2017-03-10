#!/usr/bin/python

def is_substring(s1,s2):
    ## s2 is the smaller string
    l1 = len(s1); l2 = len(s2)
    if l2 > l1 :
        return False
    for i in range(l1 - l2 + 1):
        if s1[i: i+l2] == s2:
            return True
    return False

def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1 + s1, s2)


