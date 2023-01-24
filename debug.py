from collections import Counter
import sys
import numpy as np


# dict, np.array 크기 비교

# d = {}
# for i in range(291):
#     d[i] = Counter({i : 1, i + 1 : 1})


# a = np.zeros((291,291))

# print(sys.getsizeof(d))
# print(sys.getsizeof(a))


# print(sys.getsizeof(1))
# print(sys.getsizeof(chr(1)))


def copy(object):
    return {k: v.copy() for (k, v) in object.items()}

d1 = {'a' : Counter({'b' : 1, 'a' : 2})}
print(id(d1['a']))
print(id(copy(d1)['a']))
