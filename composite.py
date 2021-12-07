'''
Returns the composite numbers of a given range.
'''

from miller_rabin import miller_rabin

upto = 1
witness = 100


def composite(int, a):
    results = []

    for i in range(int + 1):
        if miller_rabin(i, a) == False:
            results.append(i)

    return results


print(composite(upto, witness))
