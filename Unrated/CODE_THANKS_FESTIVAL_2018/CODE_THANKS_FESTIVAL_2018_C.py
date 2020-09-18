# https://atcoder.jp/contests/code-thanks-festival-2018-open/submissions/16819617
# C - Pair Distance
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    X = sorted(list(map(int, input().split())), reverse=True)

    R = [0] + list(accumulate(X))
    res = 0
    for i in range(n):
        sec_sum = R[n] - R[i + 1]
        res += X[i] * (n - (i + 1)) - sec_sum
    print(res)


if __name__ == '__main__':
    resolve()
