# https://atcoder.jp/contests/abc147/submissions/16969593
# E - Balanced Path
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    B = [list(map(int, input().split())) for _ in range(H)]

    dp = [[set() for _ in range(W)] for _ in range(H)]
    dp[0][0] = {abs(A[0][0] - B[0][0])}
    for h in range(H):
        for w in range(W):
            a, b = A[h][w], B[h][w]
            if w - 1 >= 0:
                for num in dp[h][w - 1]:
                    dp[h][w].add(abs(num + a - b))
                    dp[h][w].add(abs(-num + a - b))
            if h - 1 >= 0:
                for num in dp[h - 1][w]:
                    dp[h][w].add(abs(num + a - b))
                    dp[h][w].add(abs(-num + a - b))

    res = f_inf
    for num in dp[-1][-1]:
        res = min(res, abs(num))
    print(res)


if __name__ == '__main__':
    resolve()
