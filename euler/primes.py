import time
import numpy as np

"""
Module for prime related computations

Includes:
    Infinite prime iterator
    Thresholded prime iterator
    Primality test
    Prime Factorization
    Divisor Computation
    Divisor Cardinality
"""

class EratosthenesSieve(object):
    """
    Dynamic Sieve of Eratosthenes for prime related computations

    Attributes:
        threshold:  current size of the sieve
        primes:     list with known prime numbers
        table:      sieve table. 0:Composite 1:Prime
        rate:       rate of expansion of the sieve table
        lastnumber: last checked number in the sieve
    """

    def __init__(self,init_thr=1000,rate=10,sqrt_thr=False):
        """
        Dynamic Eratosthenes Sieve for prime generation and factorization

        Args:
            init_thr:   initial size of the sieve table
            rate:       rate of expansion of the sieve table
            sqrt_thr:   if True square root of init_thr is used instead
        """
        if not sqrt_thr:
            self.threshold = int(init_thr)
        else:
            self.threshold = int(init_thr**0.5)+1
        self.primes = []
        self.table = np.ones(self.threshold,dtype=np.int64)
        self.table[[0,1]] = 0
        self.rate=rate
        self.lastnumber=1

    def _resize_table(self):
        """
        Create a new table for the size self.rate times bigger
        the previous one
        """
        self.threshold *= self.rate
        self.table = np.ones(self.threshold,dtype=np.int64)
        for p in self.primes:
            self.table[p*p:self.threshold:p] = 0
    
    def _next_prime(self,limit=0):
        """
        Computes the next prime greater than the limit

        Resizes the sieve table as needed
    
        Args:
            limit: stopping criteria for prime generation
        Returns:
            The next prime larger than the limit
        """
        while(True):
            for p in range(self.lastnumber,self.threshold):
                if self.table[p] == 1:
                    self.primes.append(p)
                    self.lastnumber = p+1
                    self.table[p*p:self.threshold:p] = 0
                    if p > limit:
                        return p
            else:
                self.lastnumber = self.threshold
                self._resize_table()

    def __next__(self,limit=0):
        return self._next_prime()
        
    def __iter__(self):
        return self
    
    def below(self,threshold):
        """
        Iterator of primes p < threshold

        Args:
            threshold: stopping criteria for prime generation
        Returns:
            generator object for primes p < threshold
        """
        threshold = int(threshold)
        if threshold > self.lastnumber:
            self._next_prime(threshold)
        for p in self.primes[:-1]:
            yield p

    def is_prime(self,num):
        """
        Primality check for an integer number

        Args:
            num: number to be checked
        Returns:
            True if prime, False otherwise
        """
        if num < self.threshold:
            return self.table[num] == 1
        for p in self.below(int(num**0.5)+1):
            if num % p == 0:
                return False
        else:
            return True

    def factor(self,num):
        """
        Prime factorization of num

        Args:
            num: number to be factored
        Returns:
            list of tuples (prime,exponent)
        """
        num = int(num)
        F = []
        max_factor = int(num**0.5+1)
        for p in self.below(max_factor):
            if num > 1:
                i=0
                while num%p == 0:
                    i+=1
                    num //= p
                if i > 0:
                    F.append((p,i))
            else:
                break
        if num > 1:
            F += [(num,1)]
        
        return F

    def num_divisors(self,num):
        """
        Cardinality of the divisor set of num

        Does not compute the divisors so it is faster

        Args:
            num: number from which we get the divisors
        Returns:
            integer representing the number of divisors
        """
        d = self.factor(int(num))
        return np.product([ b+1 for a,b in d])

    def divisors(self,n):
        """
        Iterator over the divisors of num

        Args:
            num: number whose divisors we want to computes
        Returns:
            generator object over the divisors
        """
        def divisorsRecurrence(L):
            if L == []:
                yield 1
            else:
                (a,b) = L[0]
                for d in divisorsRecurrence(L[1:]):
                    acc = 1
                    for i in range(b+1):
                        yield d*acc
                        acc *= a

        F = self.factor(n)
        return divisorsRecurrence(F)

def primes_below(limit):
    limit = int(limit)
    primes = np.ones(limit,dtype=np.int64)
    primes[[0,1]] = 0
    for (i, isprime) in enumerate(primes):
        if isprime == 1:
            yield i
            primes[i*i:limit:i] = 0
    