# https://atcoder.jp/contests/past201912-open/submissions/18841959
# N - 整地
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, w, c = map(int, input().split())
    LRP = [list(map(int, input().split())) for _ in range(n)]

    event = [(0, 0)]
    for l, r, p in LRP:
        event.append((r, -p))
        event.append((l - c, p))
    event.sort()

    cost = 0
    res = f_inf
    for x, p in event:
        cost += p
        if 0 <= x <= w - c:
            res = min(res, cost)
    print(res)


if __name__ == '__main__':
    resolve()
