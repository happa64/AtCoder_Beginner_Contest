# https://atcoder.jp/contests/pakencamp-2019-day3/submissions/11248057
# C - カラオケ
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    res = 0
    for i in range(m):
        for j in range(i + 1, m):
            score = 0
            for k in range(n):
                score += max(a[k][i], a[k][j])
            res = max(res, score)

    print(res)


if __name__ == '__main__':
    resolve()
