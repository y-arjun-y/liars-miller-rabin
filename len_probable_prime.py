'''
Returns the length of prime numbers of a given range.
'''

from miller_rabin import miller_rabin

upto = 100
witness = 2


def len_probable_primes(int, a):
    results = []

    for i in range(int + 1):
        if miller_rabin(i, a) == True:
            results.append(miller_rabin(i, a))

    return len(results)


print(len_probable_primes(upto, witness))
