# https://atcoder.jp/contests/abc089/submissions/13980947
# D - Practical Skill Test
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    H, W, d = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    q = int(input())

    # 各数字の座標を調べる
    XY = [[] for _ in range(H * W)]
    for h in range(H):
        for w in range(W):
            XY[A[h][w] - 1] = [h, w]

    # 累積和
    R = [0] * (H * W + 1)
    for i in range(1, H * W + 1):
        if i - d > 0:
            x1, y1 = XY[i - 1]
            x2, y2 = XY[i - 1 - d]
            cost = abs(x1 - x2) + abs(y1 - y2)
            R[i] = R[i - d] + cost

    # クエリ処理
    for _ in range(q):
        l, r = map(int, input().split())
        res = R[r] - R[l]
        print(res)


if __name__ == '__main__':
    resolve()
