#!/usr/bin/python
import time
import numpy as np

def rotate_matrix(m):
    n = len(m)
    for i in range(int(n/2)):
        for j in range(i, n - i - 1):
            temp = m[i][j]                              ## temp = top
            m[i][j] = m[n - 1 - j][i]                   ## top = left
            m[n - 1 - j][i] = m[n - 1 - i][n - 1 - j]   ## left = bottom
            m[n - 1 - i][n - 1 - j] = m[j][n - 1 - i]   ## bottom = right
            m[j][n - 1 - i] = temp                      ## right = temp
    return m

inp = [[1,2],[3,4]]
inp = [[1,2,3],[4,5,6],[7,8,9]]
inp = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

inp = np.random.rand(3000,3000)
t0 = time.time()
out = np.array(rotate_matrix(inp))
print '3000: %s seconds' % (time.time() - t0)

inp = np.random.rand(100,100)
t0 = time.time()
out = np.array(rotate_matrix(inp))
print '100: %s seconds' % (time.time() - t0)

## O(N2) is observed!



