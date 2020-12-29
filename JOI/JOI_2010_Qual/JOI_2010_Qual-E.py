# https://atcoder.jp/contests/joi2010yo/submissions/19047614
# E - 通勤経路
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 100000


def resolve():
    H, W = map(int, input().split())

    dp = [[[0] * W for _ in range(H)] for _ in range(W)]
    for w in range(W):
        dp[w][0][0] = 1

    for h in range(1, H):
        nxt = [[[0] * W for _ in range(H)] for _ in range(W)]
        for w in range(W):
            if h == 1 and w == 0:
                nxt[w][0][0] = 1
                continue
            for i in range(h + 1):
                for j in range(w + 1):
                    if j == w:
                        nxt[w][i][j] += dp[w][i][j]
                        nxt[w][i][j] %= mod
                    else:
                        if (i == 0 and j == 0) or w - j > 1:
                            nxt[w][h - 1][w] += dp[w][i][j]
                            nxt[w][h - 1][w] %= mod
                    if i == h:
                        nxt[w][i][j] += nxt[w - 1][i][j]
                        nxt[w][i][j] %= mod
                    else:
                        if (i == 0 and j == 0) or h - i > 1:
                            nxt[w][h][w - 1] += nxt[w - 1][i][j]
                            nxt[w][h][w - 1] %= mod
        dp = nxt

    res = 0
    for i in range(H):
        for j in range(W):
            res += dp[-1][i][j]
            res %= mod
    print(res)


if __name__ == '__main__':
    resolve()
