# https://atcoder.jp/contests/gigacode-2019/submissions/15235174
# D - 家の建設
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, K, V = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    R = [[0] * (W + 1) for _ in range(H + 1)]
    for h in range(H):
        for w in range(W):
            R[h + 1][w + 1] = R[h][w + 1] + R[h + 1][w] - R[h][w] + A[h][w]

    res = 0
    for y1 in range(H + 1):
        for y2 in range(y1 + 1, H + 1):
            for x1 in range(W + 1):
                for x2 in range(x1 + 1, W + 1):
                    area = (y2 - y1) * (x2 - x1)
                    cost = R[y2][x2] - R[y1][x2] - R[y2][x1] + R[y1][x1]
                    cost += area * K
                    if cost <= V:
                        res = max(res, area)
    print(res)


if __name__ == '__main__':
    resolve()
