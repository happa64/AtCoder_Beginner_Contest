# https://atcoder.jp/contests/abc072/submissions/12823510
# C - Together
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    for i in range(n):
        A.append(A[i] - 1)
        A.append(A[i] + 1)

    D = Counter(A)
    res = 0
    for v in D.values():
        res = max(res, v)

    print(res)


if __name__ == '__main__':
    resolve()
