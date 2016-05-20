#!/usr/bin/env python

"""
Project Euler Problem 25
========================

   The Fibonacci sequence is defined by the recurrence relation:

     F[n] = F[n−1] + F[n−2], where F[1] = 1 and F[2] = 1.

   Hence the first 12 terms will be:

     F[1] = 1
     F[2] = 1
     F[3] = 2
     F[4] = 3
     F[5] = 5
     F[6] = 8
     F[7] = 13
     F[8] = 21
     F[9] = 34
     F[10] = 55
     F[11] = 89
     F[12] = 144

   The 12th term, F[12], is the first term to contain three digits.

   What is the first term in the Fibonacci sequence to contain 1000 digits?

Reasoning
---------
    Naive approach is fast enough but we can do better.
    Since Fib(x) ~= Phi**(x-3) we can just express the problem as
    log_Phi(10**n) = n/log_10(phi)
"""

__solution__ = "a376802c0811f1b9088828288eb0d3f0"

from math import log10,ceil

def fibonacci():
    a, b = 0,1
    while(True):
        yield a
        a,b = b, a + b

def first_fib_digits(n):
    for i,f in enumerate(fibonacci()):
        if len(str(f)) >= n:
            return i

def first_fib_digits(n):
    phi = (1+5**0.5) / 2
    return ceil((N)/log10(phi))-3

if __name__ == '__main__':
    N = 1000
    print(first_fib_digits(N))
