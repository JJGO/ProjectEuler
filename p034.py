#!/usr/bin/env python

"""
Project Euler Problem 34
========================

   145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

   Find the sum of all numbers which are equal to the sum of the factorial of
   their digits.

   Note: as 1! = 1 and 2! = 2 are not sums they are not included.

Reasoning
---------
    We can upper bound the number of digits to consider since if they were all
    nines, we would have d*9! and this has to be greater than 10**(d-1) or otherwise
    the sum would have less than d digits. We can thus solve the equation
        d*9! > 10**(d-1)
    Or more simply, just iterate until d * 9! is larger and use that d as an strict upper bound
    
    Then, we can look at combinations with replacement since the sum is commutative and it will
    reduce the search space
"""

__solution__ = "60803ea798a0c0dfb7f36397d8d4d772"

from math import factorial
import itertools

def factorial_digits():
    d = next(itertools.dropwhile(lambda d: d*factorial(9) > 10**(d-1) , itertools.count(start=2) ))
    numbers = []
    for j in range(2,d):
        for digits in itertools.combinations_with_replacement(range(10),j):
            num = sum( factorial(i) for i in digits)
            digits_sum = tuple([ int(i) for i in sorted(str(num))])
            if digits == digits_sum:
                numbers.append(num)
    return numbers

def main():
    return sum(factorial_digits())

if __name__ == '__main__':
    print(main())

