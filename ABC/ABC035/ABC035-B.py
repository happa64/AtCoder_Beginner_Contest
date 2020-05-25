# https://atcoder.jp/contests/abc035/submissions/13589151
# B - ドローン
import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    s = input()
    t = int(input())

    D = Counter(s)
    x, y = 0, 0
    cnt = 0
    for k, v in D.items():
        if k == "U":
            y += v
        elif k == "R":
            x += v
        elif k == "D":
            y -= v
        elif k == "L":
            x -= v
        else:
            cnt += v

    if t == 1:
        res = abs(x) + abs(y) + cnt
        print(res)
    else:
        dist = abs(x) + abs(y)
        if dist >= cnt:
            res = dist - cnt
            print(res)
        else:
            diff = cnt - dist
            print(0) if diff % 2 == 0 else print(1)


if __name__ == '__main__':
    resolve()
