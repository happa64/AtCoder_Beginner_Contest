# https://atcoder.jp/contests/abc018/submissions/15579681
# C - 菱型カウント
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, K = map(int, input().split())
    S = [input() for _ in range(H)]

    imos = [[0] * (W + 1) for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] == 'x':
                for k in range(K):
                    if h - k >= 0:
                        imos[h - k][max(0, w - K + 1 + k)] += 1
                        imos[h - k][min(W - 1, w + K - k)] -= 1
                    if h + k < H:
                        imos[h + k][max(0, w - K + 1 + k)] += 1
                        imos[h + k][min(W - 1, w + K - k)] -= 1
    for h in range(H):
        for w in range(1, W + 1):
            imos[h][w] += imos[h][w - 1]

    res = 0
    for h in range(K - 1, H - K + 1):
        for w in range(K - 1, W - K + 1):
            if imos[h][w] == 0:
                res += 1
    print(res)


if __name__ == '__main__':
    resolve()
