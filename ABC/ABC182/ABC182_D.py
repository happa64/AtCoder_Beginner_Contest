# https://atcoder.jp/contests/abc182/submissions/17973288
# D - Wandering
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    def debug():
        res = 0
        dist = 0
        for i in range(n):
            for j in range(i + 1):
                dist += A[j]
                res = max(res, dist)
        return res

    n = int(input())
    A = list(map(int, input().split()))

    R = [0] + list(accumulate(A))

    max_R = [0]
    for i in range(1, len(R)):
        max_R.append(max(max_R[-1], R[i]))

    P = [0]
    for r in R:
        P.append(P[-1] + r)
    P.pop(0)

    res = 0
    for i in range(len(max_R) - 1):
        res = max(res, P[i] + max_R[i])
    res = max(res, max(P))
    print(res)


if __name__ == '__main__':
    resolve()
