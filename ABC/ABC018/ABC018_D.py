# https://atcoder.jp/contests/abc018/submissions/16613724
# D - バレンタインデー
import sys
from itertools import combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m, p, q, r = map(int, input().split())
    edge = [[0] * n for _ in range(m)]
    for _ in range(r):
        x, y, z = map(int, input().split())
        edge[y - 1][x - 1] = z

    res = 0
    for girl in combinations(list(range(n)), p):
        score = [0] * m
        for i in range(m):
            for j in girl:
                score[i] += edge[i][j]
        score.sort(reverse=True)
        res = max(res, sum(score[:q]))
    print(res)


if __name__ == '__main__':
    resolve()
