#!/usr/bin/env python

# Project Euler Problem 11

# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

import time
import numpy as np

def largest_product_grid(matrix,l):
    def _diag_matrix(matrix):
        diag = np.zeros((m+n-1,min(m,n)))
        for i in range(m):
            for j in range(n):
                diag[n-1+(i-j),min(i,j)] = matrix[i,j]
        return diag
    m,n = matrix.shape
    hor_maxprod = np.max([np.prod(matrix[:,i:i+l],axis=1) for i in range(n-l+1)])
    ver_maxprod = np.max([np.prod(matrix[i:i+l,:],axis=0) for i in range(m-l+1)])
    right_diag = _diag_matrix(matrix)
    left_diag = _diag_matrix(matrix[:,::-1])
    rdiag_maxprod = np.max([np.prod(right_diag[:,i:i+l],axis=1) for i in range(min(m,n)-l+1)])
    ldiag_maxprod = np.max([np.prod(left_diag[:,i:i+l],axis=1) for i in range(min(m,n)-l+1)])
    max_prod = max(hor_maxprod, ver_maxprod, rdiag_maxprod, ldiag_maxprod)
    return int(max_prod)


if __name__ == '__main__':
    with open('numbers.txt','r') as f:
        matrix = np.array([[int(i) for i in row.split()] for row in f.read().split('\n')])
        start = time.time()
        print(largest_product_grid(matrix,4))
        print("Done! Took %.6fs" % (time.time()-start))