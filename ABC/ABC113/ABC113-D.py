# https://atcoder.jp/contests/abc113/submissions/15821617
# D - Number of Amidakuji
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, K = map(int, input().split())
    K -= 1
    dp = [[0] * W for _ in range(H + 1)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            for bit in range(1 << (W - 1)):
                flg = True
                for mask in range(W - 2):
                    if (bit & (1 << mask)) and (bit & (1 << (mask + 1))):
                        flg = False
                if flg:
                    next_j = j
                    if bit & (1 << j):
                        next_j = j + 1
                    elif j > 0 and (bit & (1 << (j - 1))):
                        next_j = j - 1
                    dp[i + 1][next_j] = (dp[i + 1][next_j] + dp[i][j]) % mod
    print(dp[H][K])


if __name__ == '__main__':
    resolve()
