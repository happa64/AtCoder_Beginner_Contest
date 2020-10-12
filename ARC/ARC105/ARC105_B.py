# https://atcoder.jp/contests/arc105/submissions/17337985
# B - MAX-=min
import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = A[0]
    for a in A:
        res = gcd(res, a)
    print(res)


if __name__ == '__main__':
    resolve()
