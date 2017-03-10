#!/usr/bin/python

from collections import deque
import sys
import time

def string_compression_list(s):
    global list_join_time
    prev_char = None
    count = 0
    comp_list = []
    for i in s:
        if prev_char and prev_char != i:
            comp_list.append(prev_char + str(count))
            if len(comp_list) >= len(s):
                #print 'Uh oh!'
                return s
            count = 0
        prev_char = i
        count += 1

    comp_list.append(prev_char + str(count))
    if len(comp_list) < len(s):
        t0 = time.time()
        rtn = ''.join(comp_list)
        list_join_time += time.time() - t0
        return rtn
    else:
        return s



def string_compression_str(s):
    prev_char = None
    count = 0
    comp_str = ''
    for i in s:
        if prev_char and prev_char != i:
            comp_str += prev_char + str(count)
            if len(comp_str) >= len(s):
                #print 'Uh oh!'
                return s
            count = 0
        prev_char = i
        count += 1

    comp_str += prev_char + str(count)
    if len(comp_str) < len(s):
        return comp_str
    else:
        return s



def string_compression_deq(s):
    global deq_join_time
    prev_char = None
    count = 0
    comp_deq = deque()
    for i in s:
        if prev_char and prev_char != i:
            comp_deq.append(prev_char + str(count))
            if len(comp_deq) >= len(s):
                #print 'Uh oh!'
                return s
            count = 0
        prev_char = i
        count += 1

    comp_deq.append(prev_char + str(count))
    if len(comp_deq) < len(s):
        t0 = time.time()
        rtn = ''.join(comp_deq)
        deq_join_time += time.time() - t0
        return rtn
    else:
        return s

#s = raw_input()

str_time = 0
deq_time = 0
list_time = 0
deq_join_time = 0
list_join_time = 0
for line in sys.stdin.readlines():
    t0 = time.time()
    print string_compression_list(line.strip())
    list_time += time.time() - t0
    t0 = time.time()
    print string_compression_str(line.strip())
    str_time += time.time() - t0
    t0 = time.time()
    print string_compression_deq(line.strip())
    deq_time += time.time() - t0

print 'str: %s seconds' % (str_time)
print 'list: %s seconds' % (list_time)
print 'list_join: %s seconds' % (list_join_time)
print 'deq: %s seconds' % (deq_time)
print 'deq join: %s seconds' % (deq_join_time)



