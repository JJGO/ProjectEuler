#!/usr/bin/env python

"""
Project Euler Problem 28
========================

   Starting with the number 1 and moving to the right in a clockwise
   direction a 5 by 5 spiral is formed as follows:

                                 21 22 23 24 25
                                 20  7  8  9 10
                                 19  6  1  2 11
                                 18  5  4  3 12
                                 17 16 15 14 13

   It can be verified that the sum of the numbers on the diagonals is 101.

   What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
   formed in the same way?

Reasoning
---------
    Key idea is realizing that the sum of the items in each radius follows the
    expression 16n^2+4n+4.
    Naive approach uses a iterative sum of this polynomials
    Even better, we use series formulas to compute the sum of an arbitrary
    quadratic polynomial
"""

__solution__ = "0d53425bd7c5bf9919df3718c8e49fa6"

import numpy as np
from numpy.linalg import inv

def sum_diagonals_spiral(D):
    return 1+4*sum([4*n**2+n+1 for n in range(1,D//2+1)])

def solve_quadratic_poly(x,y,z):
    A = np.array([[1,1,1],[1,2,4],[1,3,9]])
    B = np.array([x,y,z]).reshape((3,1))
    return np.dot(inv(A),B).squeeze()

def sum_quad_poly(poly,N):
    sum_coeffs = [ N, N*(N+1) // 2 , N*(N+1)*(2*N+1) // 6]
    return int(np.dot(poly,sum_coeffs))

def sum_diagonals_spiral(D):
    N = D//2+1
    poly = solve_quadratic_poly(24,76,160)
    diag_sum = 1 + sum_quad_poly(poly,N-1)
    return diag_sum

def main():
    return sum_diagonals_spiral(1001)

if __name__ == '__main__':
    print(main())
