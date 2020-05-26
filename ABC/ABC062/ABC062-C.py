# https://atcoder.jp/contests/abc062/submissions/13609306
# C - Chocolate Bar
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7
res = f_inf


def resolve():
    H, W = map(int, input().split())

    def calc(A, B, C):
        global res
        ma = max(A, B, C)
        mi = min(A, B, C)
        res = min(res, ma - mi)

    for h in range(H):
        A = h * W

        B = W * ((H - h) // 2)
        C = W * ((H - h) - (H - h) // 2)
        calc(A, B, C)

        B = (H - h) * (W // 2)
        C = (H - h) * (W - W // 2)
        calc(A, B, C)

    for w in range(W):
        A = w * H

        B = H * ((W - w) // 2)
        C = H * ((W - w) - (W - w) // 2)
        calc(A, B, C)

        B = (W - w) * (H // 2)
        C = (W - w) * (H - H // 2)
        calc(A, B, C)

    print(res)


if __name__ == '__main__':
    resolve()
