# https://atcoder.jp/contests/joi2008ho/submissions/14150101
# C - ダーツ
import sys
import bisect

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    P = [0] + list(int(input()) for _ in range(n))

    point = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            point.append(P[i] + P[j])
    point.sort()

    res = 0
    for p1 in point:
        if p1 > m:
            continue
        else:
            res = max(res, p1)

        idx = bisect.bisect_left(point, m - p1)
        if idx - 1 < 0:
            continue

        p2 = point[idx - 1]
        res = max(res, p1 + p2)
        if res == m:
            break

    print(res)


if __name__ == '__main__':
    resolve()
