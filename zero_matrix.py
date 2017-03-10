#!/usr/bin/python

import numpy as np
from bitarray import bitarray

def find_zeros(m):
    rows, cols = m.shape
    zero_rows = bitarray(rows)
    zero_cols = bitarray(cols)
    for i in range(rows):
        for j in range(cols):
            if m[i][j] == 0 :
                zero_rows[i] = True
                zero_cols[j] = True
    return zero_rows, zero_cols

def make_zeros(zero_rows, zero_cols, m):
    for row, val in enumerate(zero_rows):
        if val:
            m[row, :] = 0
    for col, val in enumerate(zero_cols):
        if val:
            m[:, col] = 0

    return m

m = np.array([[1,2,3],[0,4,5],[6,7,0]])
print m
print '\n'

zero_rows, zero_cols = find_zeros(m)
m =make_zeros(zero_rows, zero_cols, m)

print m
