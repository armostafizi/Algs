#!/usr/bin/python

def replace_spaces(s):
    words = s.strip().split()
    return '%20'.join(words)

def replace_spaces_scratch(s):
    new_str = ''
    for i in range(len(s)):
        if s[i] == ' ':
            new_str += '%20'
        else:
            new_str += s[i]
    return new_str

s = raw_input()
print replace_spaces(s)
print replace_spaces_scratch(s)

