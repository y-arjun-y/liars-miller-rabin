'''
Implementation of the Miller-Rabin primality test in Python3. 
Function by https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N.
Variables and formula is based on https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test.
A return value of False means n in not prime.
A return value of True means n is very likely to be a prime.
'''


def miller_rabin(n, a):
    # checking if it is an integer
    if n != int(n):
        return False

    n = int(n)

    # base cases
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True

    if n % 2 == 0:
        return False

    # assigning variables
    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    # trial run
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False

        for i in range(s):
            if pow(a, 2**i * d, n) == n - 1:
                return False
        return True

    # number of trials, directly proportional to time and accuracy.
    num_trials = 10

    # run
    for _ in range(num_trials):
        if trial_composite(a):
            return False

    return True
