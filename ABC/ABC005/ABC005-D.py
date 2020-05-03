# https://atcoder.jp/contests/abc005/tasks/abc005_4
# D - おいしいたこ焼きの焼き方
import math, itertools, heapq, collections, bisect, sys, copy

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** + 7


def resolve():
    n = int(input())
    D = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    P = list(int(input()) for _ in range(q))

    # 二次元累積和
    R = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(n):
            R[i + 1][j + 1] = R[i][j + 1] + R[i + 1][j] - R[i][j] + D[i][j]

    # 一度に作れる数がareaの時の美味しさの最大値を計算
    res = [0 for _ in range(n * n + 1)]
    for x1 in range(n):
        for x2 in range(x1 + 1, n + 1):
            for y1 in range(n):
                for y2 in range(y1 + 1, n + 1):
                    area = (x2 - x1) * (y2 - y1)
                    sum = R[x2][y2] - R[x1][y2] - R[x2][y1] + R[x1][y1]
                    res[area] = max(res[area], sum)

    # 一度に作れる数がarea"以下"の時の美味しさの最大値を集計
    for i in range(n * n):
        res[i + 1] = max(res[i + 1], res[i])

    for i in P:
        print(res[i])


if __name__ == '__main__':
    resolve()
