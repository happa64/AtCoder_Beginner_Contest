# https://atcoder.jp/contests/typical90/submissions/22982454
# 052 - Dice Product（★3）
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    n = int(input())
    A = [list(map(int, input().split())) for _ in range(n)]

    res = 1
    for a in A:
        res *= sum(a) % MOD
        res %= MOD
    print(res)


if __name__ == '__main__':
    solve()
