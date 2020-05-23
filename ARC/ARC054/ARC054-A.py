# https://atcoder.jp/contests/arc054/submissions/13494075
# A - 動く歩道
import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    l, x, y, s, d = map(int, input().split())

    if s <= d:
        dist1 = d - s
        res1 = dist1 / (x + y)
        if y - x > 0:
            dist2 = s + l - d
            res2 = dist2 / (y - x)
            print(min(res1, res2))
        else:
            print(res1)
    else:
        dist1 = l - s + d
        res1 = dist1 / (x + y)
        if y - x > 0:
            dist2 = s - d
            res2 = dist2 / (y - x)
            print(min(res1, res2))
        else:
            print(res1)


if __name__ == '__main__':
    resolve()
