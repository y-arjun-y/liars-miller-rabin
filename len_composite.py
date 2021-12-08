'''
Returns the length of composite numbers of a given range.
'''

from miller_rabin import miller_rabin

def len_composite(int, a):
    results = []

    for i in range(int + 1):
        if miller_rabin(i, a) == False:
            results.append(miller_rabin(i, a))

    return len(results)
