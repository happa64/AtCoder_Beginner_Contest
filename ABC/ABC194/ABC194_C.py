# https://atcoder.jp/contests/abc194/submissions/20708255
# C - Squared Error
import sys
from itertools import accumulate

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = list(map(int, input().split()))
    R = [0] + list(accumulate(A))
    m = 0
    for i in range(n):
        diff = R[-1] - R[i + 1]
        m += 2 * A[i] * diff

    pow2 = [0]
    for i in range(n):
        pow2.append(pow2[-1] + A[i] ** 2)

    p = 0
    for i in range(n):
        p += (n - 1) * pow(A[i], 2)
    res = p - m
    print(res)


if __name__ == '__main__':
    solve()
