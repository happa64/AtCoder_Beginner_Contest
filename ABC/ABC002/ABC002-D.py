# https://atcoder.jp/contests/abc002/submissions/14177833
# D - 派閥
import sys
from itertools import product, combinations

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def resolve():
    n, m = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(m)]

    res = 0
    for pattern in product([0, 1], repeat=n):
        f = []
        for idx, p in enumerate(pattern):
            if p == 1:
                f.append(idx + 1)
        for x, y in combinations(f, 2):
            if [x, y] not in XY:
                break
        else:
            res = max(res, sum(pattern))

    print(res)


if __name__ == '__main__':
    resolve()
