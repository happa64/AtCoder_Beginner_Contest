# https://atcoder.jp/contests/maximum-cup-2018/submissions/20069928
# D - Many Go Round
import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, l, x = map(int, input().split())
    A = tuple(map(int, input().split()))
    dp = [f_inf] * m
    dp[0] = 1
    for a in A:
        ndp = deepcopy(dp)
        for i in range(m):
            if dp[i] != f_inf:
                q, r = divmod(i + a, m)
                ndp[r] = min(ndp[r], dp[i] + q)
        dp = ndp
    print("Yes" if 1 <= dp[l] <= x else "No")


if __name__ == '__main__':
    resolve()
