# https://atcoder.jp/contests/abc081/submissions/13620229
# B - Shift only
import sys
import numpy as np
from collections import Counter, deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = np.array(list(map(int, input().split())))

    res = 0
    while not any(np.mod(A, 2)):
        res += 1
        A //= 2

    print(res)


if __name__ == '__main__':
    resolve()
