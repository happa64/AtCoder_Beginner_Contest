# https://atcoder.jp/contests/abc012/submissions/13279151
# D - バスと避けられない運命
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())

    # ワーシャルフロイド法でバス停間の最短距離を計算
    T = [[f_inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        T[i][i] = 0

    for _ in range(m):
        a, b, t = map(int, input().split())
        T[a - 1][b - 1] = t
        T[b - 1][a - 1] = t

    for k in range(n):
        for i in range(n):
            for j in range(n):
                T[i][j] = min(T[i][j], T[i][k] + T[k][j])

    res = f_inf
    for i in T:
        max_dist = max(i)
        res = min(res, max_dist)

    print(res)


if __name__ == '__main__':
    resolve()
