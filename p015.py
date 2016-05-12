#!/usr/bin/env python

"""
Project Euler Problem 15
========================

   Starting in the top left corner of a 2×2 grid, and only being able to move
   to the right and down, there are exactly 6 routes to the bottom right
   corner.

   How many such routes are there through a 20×20 grid?

   
   p_015.gif

Reasoning
---------
    We can matemathically solve the problem in a nxn grid as (2*N choose N)
    because if we know the positions of DOWN movements, RIGHT are implicit
    and since there will always be 2*N movements in total we are choosing
    n indeces out of 2*N and thus (2*N choose N)

    Another way of reasoning it is that if we have N identical DOWN elements
    and N identical RIGHT elements and we want the number of unique permutations.
    This is solved by considering them different and then dividing for the number
    of permutations: 2N!/(N*!N!) = (2*N choose N)

    Finally a slower dynamic programming approach can be used in which the number
    of paths of getting to P(m,n) = P(m-1,n)+P(m,n-1) and P(0,n) = 1, P(m,0) = 1
"""

__solution__ = "928f3957168ac592c4215dcd04e0b678"


import operator as op
from functools import reduce
import numpy as np

def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, range(n, n-r, -1))
    denom = reduce(op.mul, range(1, r+1))
    return numer//denom

def num_paths(m,n):
    return ncr(m+n,m)

def num_paths2(m,n):
    num_paths = np.zeros([m+1,n+1],dtype=int)
    num_paths[:,0] = 1
    num_paths[0,:] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
          num_paths[i,j] = num_paths[i-1,j] + num_paths[i,j-1]
    return num_paths[m,n]

if __name__ == '__main__':
    print(num_paths(20,20))