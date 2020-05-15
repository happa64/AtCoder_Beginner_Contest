# https://atcoder.jp/contests/abc071/submissions/11773020
# C - Make a Rectangle
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    _ = int(input())
    A = list(map(int, input().split()))

    D = Counter(A)
    res = []
    for k, v in D.items():
        if v >= 2:
            for _ in range(v // 2):
                res.append(k)

    if len(res) < 2:
        print(0)
    else:
        res = sorted(res, reverse=True)
        print(res[0] * res[1])


if __name__ == '__main__':
    resolve()
