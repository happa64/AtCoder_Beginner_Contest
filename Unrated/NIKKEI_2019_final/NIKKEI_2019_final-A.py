# https://atcoder.jp/contests/nikkei2019-final/submissions/15223140
# A - Abundant Resources
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    R = [0] + list(accumulate(A))

    for k in range(1, n + 1):
        res = 0
        for left in range(n - k + 1):
            right = left + k
            res = max(res, R[right] - R[left])
        print(res)


if __name__ == '__main__':
    resolve()
