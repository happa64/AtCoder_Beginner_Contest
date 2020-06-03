# https://atcoder.jp/contests/agc043/submissions/me
# A - Range Flip Find Route
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    # 白と黒が入れ替わった箇所をカウントする
    flip = [[f_inf for _ in range(W)] for _ in range(H)]

    if S[0][0] == "#":
        flip[0][0] = 1
    else:
        flip[0][0] = 0

    # 幅優先探索
    que = deque([[0, 0]])
    while que:
        h, w = que.popleft()
        for dh, dw in ((0, 1), (1, 0)):
            next_h, next_w = h + dh, w + dw
            if next_h >= H or next_w >= W:
                continue

            if flip[next_h][next_w] == f_inf:
                que.append([next_h, next_w])

            # 白と黒が入れ替わったらカウントアップ
            # 各座標のカウントは常に最小の数値に更新していく（動的計画法）
            if S[h][w] != S[next_h][next_w]:
                flip[next_h][next_w] = min(flip[next_h][next_w], flip[h][w] + 1)
            else:
                flip[next_h][next_w] = min(flip[next_h][next_w], flip[h][w])

    if S[H - 1][W - 1] == "#":
        flip[H - 1][W - 1] += 1

    # 操作の回数は白と黒が入れ替わった回数の半分（切り捨て）である
    print(flip[H - 1][W - 1] // 2)


if __name__ == '__main__':
    resolve()
