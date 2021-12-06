'''
Calculates the length of composite numbers of a given range.
'''

from miller_rabin import miller_rabin


def len_composite(int):
    results = []
    false_results = []

    for i in range(int + 1):
        results.append(miller_rabin(i))

    for i in results:
        if i == False:
            false_results.append(i)

    return len(false_results)


print(len_composite(1000000000))
