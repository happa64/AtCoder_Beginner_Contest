# https://atcoder.jp/contests/ddcc2020-qual/submissions/14513195
# C - Strawberry Cakes
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, K = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    res = [[0] * W for _ in range(H)]
    num = 0
    for h in range(H):
        flg = 0
        for w in range(W):
            if S[h][w] == "#":
                num += 1
                flg = 1
            res[h][w] = num if flg else 0

    for h in range(H):
        num = res[h][-1]
        for w in reversed(range(W)):
            if S[h][w] == "#":
                num = res[h][w]
            res[h][w] = num

    for w in range(W):
        for h in range(1, H):
            if res[h][w] == 0:
                res[h][w] = res[h - 1][w]

    for w in range(W):
        for h in reversed(range(H - 1)):
            if res[h][w] == 0:
                res[h][w] = res[h + 1][w]

    for i in res:
        print(*i)


if __name__ == '__main__':
    resolve()
