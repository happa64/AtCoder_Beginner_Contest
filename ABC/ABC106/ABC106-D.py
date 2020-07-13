# https://atcoder.jp/contests/abc106/submissions/15225658
# D - AtCoder Express 2
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, q = map(int, input().split())
    cnt = [[0] * n for _ in range(n)]
    for _ in range(m):
        l, r = map(int, input().split())
        cnt[l - 1][r - 1] += 1

    R = [[0] * (n + 1) for _ in range(n + 1)]
    for h in range(n):
        for w in range(n):
            R[h + 1][w + 1] = R[h][w + 1] + R[h + 1][w] - R[h][w] + cnt[h][w]

    for _ in range(q):
        p, q = map(int, input().split())
        res = R[q][q] - R[p - 1][q] - R[q][p - 1] + R[p - 1][p - 1]
        print(res)


if __name__ == '__main__':
    resolve()
