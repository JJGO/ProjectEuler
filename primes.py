

def primes_sieve(limit):
    a = [False] * 2 + [True] * (limit-2)      # Initialize the primality list
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def is_prime(num):
    for p in primes_sieve(int(num**0.5)+1):
        if num % p == 0:
            return False
    else:
        return True