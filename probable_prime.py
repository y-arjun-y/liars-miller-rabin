'''
Returns the probable prime numbers of a given range.
'''

from miller_rabin import miller_rabin

upto = 100
witness = 2


def probable_primes(int, a):
    results = []

    for i in range(int + 1):
        if miller_rabin(i, a) == True:
            results.append(i)

    return results


print(probable_primes(upto, witness))
