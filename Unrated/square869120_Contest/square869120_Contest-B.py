# https://atcoder.jp/contests/s8pc-4/submissions/14936135
# B - Buildings are Colorful!
import sys
from itertools import product
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A_init = list(map(int, input().split()))

    res = f_inf
    for pattern in product([0, 1], repeat=n - 1):
        A = deepcopy(A_init)
        cost = 0
        for idx, p in enumerate(pattern):
            if p == 1:
                prev = max([A[i] for i in range(idx + 1)])
                if A[idx + 1] > prev:
                    continue
                cost += prev + 1 - A[idx + 1]
                A[idx + 1] = prev + 1
        cnt = mi = 0
        for a in A:
            if mi < a:
                mi = a
                cnt += 1
        if cnt >= k:
            res = min(res, cost)
    print(res)


if __name__ == '__main__':
    resolve()
