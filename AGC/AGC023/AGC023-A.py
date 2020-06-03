# https://atcoder.jp/contests/agc023/tasks/agc023_a
# A - Zero-Sum Ranges
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    R = [0]
    for i in range(n):
        R.append(R[-1] + A[i])

    D = Counter(R)
    res = 0
    for v in D.values():
        res += v * (v - 1) // 2

    print(res)


if __name__ == '__main__':
    resolve()
