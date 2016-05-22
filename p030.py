#!/usr/bin/env python

"""
Project Euler Problem 30
========================

   Surprisingly there are only three numbers that can be written as the sum
   of fourth powers of their digits:

     1634 = 1^4 + 6^4 + 3^4 + 4^4
     8208 = 8^4 + 2^4 + 0^4 + 8^4
     9474 = 9^4 + 4^4 + 7^4 + 4^4

   As 1 = 1^4 is not a sum it is not included.

   The sum of these numbers is 1634 + 8208 + 9474 = 19316.

   Find the sum of all the numbers that can be written as the sum of fifth
   powers of their digits.

Reasoning
---------
    We can upper bound the number of digits to consider since if they were all
    nines, we would have d*9**n and this has to be greater than 10**(d-1) or otherwise
    the sum would have less than d digits. We can thus solve the equation
        d*9^n > 10^(d-1)
    Or more simply, just iterate until d * 9**n is larger and use that d as an strict upper bound
    
    Then, we can look at combinations with replacement since the sum is commutative and it will
    reduce the search space
"""

__solution__ = "27a1779a8a8c323a307ac8a70bc4489d"

import itertools

def power_digits(n):
    d = next(itertools.dropwhile(lambda d: d*9**n > 10**(d-1) , itertools.count(start=2) ))
    numbers = []
    for j in range(2,d):
        for digits in itertools.combinations_with_replacement(range(10),j):
            num = sum( i**n for i in digits)
            digits_sum = tuple([ int(i) for i in sorted(str(num))])
            if digits == digits_sum:
                numbers.append(num)
    return numbers

def main():
    return sum(power_digits(5))

if __name__ == '__main__':
    assert( sum(power_digits(4)) == 19316)
    print(main())

