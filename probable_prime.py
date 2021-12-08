'''
Returns the probable prime numbers of a given range.
'''

from miller_rabin import miller_rabin

def probable_primes(int, a):
    results = []

    for i in range(int + 1):
        if miller_rabin(i, a) == True:
            results.append(i)

    return results
