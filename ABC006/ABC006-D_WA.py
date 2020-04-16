# https://atcoder.jp/contests/abc006/tasks/abc006_4
# D - トランプ挿入ソート（10点解法）
import sys
from itertools import product

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    C = list(int(input()) for _ in range(n))

    # 抜き取るパターンを全探索し、抜き取った後の増加列が最長となるパターンが答えとなる
    res = f_inf
    for pattern in product([0, 1], repeat=n):
        c = []
        for idx, p in enumerate(pattern):
            if p == 0:
                c.append(C[idx])
        if c == sorted(c):
            res = min(res, len(C) - len(c))

    print(res)


if __name__ == '__main__':
    resolve()
