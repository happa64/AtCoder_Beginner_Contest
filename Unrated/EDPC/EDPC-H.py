# https://atcoder.jp/contests/dp/submissions/13656397
# H - Grid 1
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(input().rstrip()) for _ in range(H)]

    dp = [[f_inf] * W for _ in range(H)]
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if A[h][w] != "#":
                if h - 1 >= 0 and w - 1 >= 0:
                    dp[h][w] = min(dp[h][w], ((dp[h - 1][w] if A[h - 1][w] == "." else 0) + (dp[h][w - 1] if A[h][w - 1] == "." else 0)) % mod)
                elif h - 1 >= 0:
                    dp[h][w] = min(dp[h][w], (dp[h - 1][w] if A[h - 1][w] == "." else 0) % mod)
                elif w - 1 >= 0:
                    dp[h][w] = min(dp[h][w], (dp[h][w - 1] if A[h][w - 1] == "." else 0) % mod)

    print(dp[H - 1][W - 1] % mod)


if __name__ == '__main__':
    resolve()
