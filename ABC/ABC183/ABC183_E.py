# https://atcoder.jp/contests/abc183/submissions/18147757
# E - Queen on Grid
import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = list(input().rstrip() for _ in range(H))

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    y = 1
    for w in range(1, W):
        if S[0][w] == "#":
            break
        dp[0][w] += y
        dp[0][w] %= mod
        y += dp[0][w]
        y %= mod

    t = 1
    for h in range(1, H):
        if S[h][0] == "#":
            break
        dp[h][0] += t
        dp[h][0] %= mod
        t += dp[h][0]
        t %= mod

    yoko = deepcopy(dp)
    tate = deepcopy(dp)
    naname = deepcopy(dp)

    for h in range(1, H):
        for w in range(1, W):
            if S[h][w] == "#":
                continue
            dp[h][w] = (yoko[h][w - 1] + tate[h - 1][w] + naname[h - 1][w - 1]) % mod
            yoko[h][w] = (yoko[h][w - 1] + dp[h][w]) % mod
            tate[h][w] = (tate[h - 1][w] + dp[h][w]) % mod
            naname[h][w] = (naname[h - 1][w - 1] + dp[h][w]) % mod

    print(dp[-1][-1] % mod)


if __name__ == '__main__':
    resolve()
