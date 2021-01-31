# https://atcoder.jp/contests/abc190/submissions/19780990
# C - Bowls and Dishes
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]
    k = int(input())
    CD = [list(map(int, input().split())) for _ in range(k)]

    res = 0
    for pattern in product([0, 1], repeat=k):
        t = set()
        for i, p in enumerate(pattern):
            t.add(CD[i][p])
        cnt = 0
        for a, b in AB:
            if a in t and b in t:
                cnt += 1
        res = max(res, cnt)
    print(res)


if __name__ == '__main__':
    resolve()
