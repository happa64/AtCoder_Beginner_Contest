# https://atcoder.jp/contests/pakencamp-2020-day1/submissions/19534903
# K - Gcd of Sum
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(accumulate(map(int, input().split())))
    MAX = A[-1] + 1

    res = [0] * n
    for i in range(1, MAX):
        if A[-1] % i == 0:
            cnt = sum(A[j] % i == 0 for j in range(n))
            for j in range(cnt):
                res[j] = i
    print(*res, sep="\n")


if __name__ == '__main__':
    resolve()
