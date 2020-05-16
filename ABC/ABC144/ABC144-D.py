# https://atcoder.jp/contests/abc144/submissions/13260154
# D - Water Bottle
import sys
import math

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    a, b, x = map(int, input().split())
    s = a * (x / pow(a, 2))

    if (a * b) // 2 >= s:
        h = s * 2 / b
        res = math.degrees(math.atan(b / h))
        print(res)
    else:
        h = (a * b - s) * 2 / a
        res = math.degrees(math.atan(h / a))
        print(res)


if __name__ == '__main__':
    resolve()
