# https://atcoder.jp/contests/abc129/submissions/14428202
# D - Lamp
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = [list(list(input().rstrip())) for _ in range(H)]

    CW = [[0] * W for _ in range(H)]
    for h in range(H):
        cnt = 0
        for w in range(W):
            if S[h][w] == "#":
                cnt = 0
            else:
                cnt += 1
                CW[h][w] = cnt
        cnt = 0
        for w in reversed(range(W)):
            if S[h][w] == ".":
                cnt = max(cnt, CW[h][w])
                CW[h][w] = cnt
            else:
                cnt = 0

    CH = [[0] * W for _ in range(H)]
    for w in range(W):
        cnt = 0
        for h in range(H):
            if S[h][w] == "#":
                cnt = 0
            else:
                cnt += 1
                CH[h][w] = cnt
        cnt = 0
        for h in reversed(range(H)):
            if S[h][w] == ".":
                cnt = max(cnt, CH[h][w])
                CH[h][w] = cnt
            else:
                cnt = 0

    res = 0
    for h in range(H):
        for w in range(W):
            C = CW[h][w] + CH[h][w] - 1
            res = max(res, C)
    print(res)


if __name__ == '__main__':
    resolve()
