# https://atcoder.jp/contests/abc210/submissions/24331838
# D - National Railway
import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
MOD = 10 ** 9 + 7


def solve():
    H, W, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    res = f_inf

    dp = deepcopy(A)
    x = [[f_inf] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h - 1 >= 0:
                dp[h][w] = min(dp[h][w], dp[h - 1][w] + c)
                x[h][w] = min(x[h][w], dp[h - 1][w] + c + A[h][w])
            if w - 1 >= 0:
                dp[h][w] = min(dp[h][w], dp[h][w - 1] + c)
                x[h][w] = min(x[h][w], dp[h][w - 1] + c + A[h][w])
            res = min(res, x[h][w])

    A = [A[h][::-1] for h in range(H)]

    dp = deepcopy(A)
    x = [[f_inf] * W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if h - 1 >= 0:
                dp[h][w] = min(dp[h][w], dp[h - 1][w] + c)
                x[h][w] = min(x[h][w], dp[h - 1][w] + c + A[h][w])
            if w - 1 >= 0:
                dp[h][w] = min(dp[h][w], dp[h][w - 1] + c)
                x[h][w] = min(x[h][w], dp[h][w - 1] + c + A[h][w])
            res = min(res, x[h][w])

    print(res)


if __name__ == '__main__':
    solve()
