# https://atcoder.jp/contests/abc202/submissions/22828336
# D - aab aba baa
import sys
from math import factorial

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def fact(n, r):
    a = factorial(n + r)
    b = factorial(n) * factorial(r)
    return a // b


def solve():
    A, B, K = map(int, input().split())
    L = A + B

    res = ""
    for i in range(L):
        if A and B:
            a = fact(A - 1, B)
            if a < K:
                K -= a
                B -= 1
                res += "b"
            else:
                A -= 1
                res += "a"
        elif A:
            res += "a" * A
            break
        else:
            res += "b" * B
            break
    print(res)


if __name__ == '__main__':
    solve()
