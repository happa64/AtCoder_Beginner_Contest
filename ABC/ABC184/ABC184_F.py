# https://atcoder.jp/contests/abc184/submissions/18346052?lang=ja
# F - Programming Contest
import sys
from itertools import product
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, T = map(int, input().split())
    A = list(map(int, input().split()))

    m = n // 2
    M = A[:m]
    kouho1 = []
    for pattern in product([0, 1], repeat=m):
        t = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                t += M[idx]
        if t <= T:
            kouho1.append(t)

    o = n - m
    O = A[m:]
    kouho2 = []
    for pattern in product([0, 1], repeat=o):
        t = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                t += O[idx]
        if t <= T:
            kouho2.append(t)

    kouho2.append(-f_inf)
    kouho2.sort()
    res = 0
    for k in kouho1:
        target = T - k
        ind = bisect_right(kouho2, target)
        res = max(res, k + kouho2[ind - 1])
    print(res)


if __name__ == '__main__':
    resolve()
