#!/usr/bin/env python

# Project Euler Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import numpy as np
import time
def sum_multiples(threshold,x,y):
	mx = np.arange(0,threshold,x)
	my = np.arange(0,threshold,y)
	mxy = np.arange(0,threshold,x*y)
	return np.sum(mx)+np.sum(my)-np.sum(mxy)

if __name__ == '__main__':
	start = time.time()
	print(sum_multiples(1000,3,5))
	print("Done! Took %.6fs" % (time.time()-start))