#!/usr/bin/env python

"""
Project Euler Problem 31
========================

   In England the currency is made up of pound, £, and pence, p, and there
   are eight coins in general circulation:

     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

   It is possible to make £2 in the following way:

     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

   How many different ways can £2 be made using any number of coins?

Reasoning
---------
    Recursion for
"""

__solution__ = "142dfe4a33d624d2b830a9257e96726d"

def coin_permutations(quantity,coins,index=0):
    if index == len(coins)-1 and coins[index] == 1:
        return 1
    elif quantity == 0:
        return 1
    elif len(coins) == 0:
        return 0
    n = 0
    for i in range(quantity // coins[index]+1):
        n += coin_permutations(quantity-i*coins[index], coins,index+1)
    return n

def main():
    return coin_permutations(200,[200,100,50,20,10,5,2,1])

if __name__ == '__main__':
    print(main())

